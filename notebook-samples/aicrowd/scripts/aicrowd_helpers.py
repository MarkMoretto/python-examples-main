# coding=utf-8

# Via: https://gitlab.aicrowd.com/jyotish/pricing-game-notebook-scripts/-/blob/master/python/aicrowd_helpers.py


from IPython.core.magic import (
    register_cell_magic,
    register_line_magic,
    needs_local_scope,
)
import json
import inspect
import os
import subprocess
import sys

SUBMISSION_DIR = "submission_dir"
CHALLENGE_URL = "https://www.aicrowd.com/challenges/insurance-pricing-game"


def execute_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    def print_output(handle):
        if handle is not None:
            output = handle.readline()
            if output:
                print(output.decode().strip())

    while True:
        if process.poll() is not None:
            break
        print_output(process.stdout)
        print_output(process.stderr)
    rc = process.poll()
    return rc


@register_cell_magic
@needs_local_scope
def track_imports(line, cell):
    with open("global_imports.py", "w") as fp:
        fp.write(cell)


@register_cell_magic
@needs_local_scope
def aicrowd_include(line, cell):
    with open("utils.py", "w") as fp:
        fp.write("from global_imports import *\n")
        fp.write(cell)


@register_cell_magic
@needs_local_scope
def track_installs(line, cell):
    with open("install.R", "w") as fp:
        fp.write(cell)


def load_submission_config(local_ns):
    if "Config" not in local_ns:
        print(
            "❗️ Could not find submission configuration. Did you run the",
            "cell with `class Config`?",
        )
    validate_submission_config(local_ns["Config"])
    return local_ns["Config"]


def validate_submission_config(cfg):
    required_attributes = ["AICROWD_API_KEY", "MODEL_OUTPUT_PATH"]
    for attr in required_attributes:
        try:
            value = getattr(cfg, attr)
            assert value != ""
        except Exception:
            print(f"❗️ {attr} should not be empty")
            sys.exit(1)


def check_submission_dir():
    if not os.path.exists(SUBMISSION_DIR):
        print(
            "❗️Base submission dir is missing. Did you run the setup cell",
            "(first cell of the notebook)?",
        )


@register_line_magic
@needs_local_scope
def aicrowd_submit(line, local_ns):
    print("🚀 Preparing to submit...")

    check_submission_dir()
    cfg = load_submission_config(local_ns)

    collect_submission_files(cfg, local_ns)

    print("💾 Preparing the submission zip file...")
    zip_submission()

    submit_to_aicrowd(cfg)
    # print("🎊🎉 Submitted to AIcrowd 🎉🎊")
    # print("\n" + "=" * 60 + "\n")
    # print(
    #     f"You can view your submission status at {CHALLENGE_URL}/submissions?my_submissions=true"
    # )


@register_line_magic
@needs_local_scope
def download_aicrowd_dataset(line, local_ns):
    print("💾 Downloading dataset...")
    cfg = load_submission_config(local_ns)
    aicrowd_login(cfg.AICROWD_API_KEY)
    return_code = execute_command("aicrowd dataset download -c insurance-pricing-game")
    if return_code != 0:
        print("🚫 Failed to download dataset 😢")
        sys.exit(return_code)
    # return_code = execute_command("mv training_v0.2.csv training.csv")
    if return_code != 0:
        print("🚫 Failed to download dataset 😢")
        sys.exit(return_code)
    print("✅ Downloaded dataset")


def collect_submission_files(cfg, local_ns):
    print("⚙️ Collecting the submission code...")
    write_aicrowd_json(cfg)
    write_requirements_txt(cfg)
    write_apt_txt(cfg)
    copy_model_file(cfg)
    return_code = execute_command(f"cp global_imports.py utils.py submission_dir")
    if return_code != 0:
        print("🚫 Failed to copy submission files 😢")
        sys.exit(return_code)
    target_fns = [
        "fit_model",
        "predict_expected_claim",
        "predict_premium",
        "load_model",
        "save_model",
    ]
    for fn_name in target_fns:
        with open(f"{SUBMISSION_DIR}/{fn_name}.py", "w") as fp:
            fp.write("from global_imports import *\n")
            fp.write("from utils import *\n")
            if fn_name == "predict_premium":
                fp.write("from predict_expected_claim import predict_expected_claim\n")
            fp.write("\n\n")
            fp.write(inspect.getsource(local_ns[fn_name]))


def write_aicrowd_json(cfg):
    config = {
        "language": "python",
        "model_path": cfg.MODEL_OUTPUT_PATH,
    }
    with open(f"{SUBMISSION_DIR}/config.json", "w") as fp:
        json.dump(config, fp)


def write_requirements_txt(cfg):
    with open(f"{SUBMISSION_DIR}/requirements.txt", "w") as fp:
        for requirement in cfg.ADDITIONAL_PACKAGES:
            fp.write(f"{requirement}\n")


def write_apt_txt(cfg):
    if getattr(cfg, "APT_PACKAGES", False):
        if isinstance(cfg.APT_PACKAGES, list):
            with open(f"{SUBMISSION_DIR}/apt.txt", "w") as fp:
                for pkg in cfg.APT_PACKAGES:
                    fp.write(f"{pkg}\n")


def zip_submission():
    cmd = [f"cd {SUBMISSION_DIR}", f"zip -r submission.zip .", f"mv submission.zip .."]
    if execute_command(" && ".join(cmd)) != 0:
        print("Failed to create submission zip file 😢")
        sys.exit(1)


def aicrowd_login(api_key):
    return_code = execute_command(f"aicrowd login --api-key {api_key}")
    if return_code != 0:
        print("🚫 Failed to login to AIcrowd 😢")
        sys.exit(1)


def submit_to_aicrowd(cfg):
    aicrowd_login(cfg.AICROWD_API_KEY)
    return_code = execute_command(
        "aicrowd submission create -c insurance-pricing-game -f submission.zip"
    )
    if return_code != 0:
        print("🚫 Failed to submit to AIcrowd 😢")
        sys.exit(1)


def copy_model_file(cfg):
    return_code = execute_command(f"cp {cfg.MODEL_OUTPUT_PATH} submission_dir")
    if return_code != 0:
        print("🚫 Failed to copy model 😢")
        sys.exit(1)
