export SUBMISSION_DIR="submission_dir"
export BRANCH="master"

execute_fn() {
    if ! eval "$@"; then
        echo "🚫 Failed to `echo $1 | tr '_' ' '` 😢"
        exit 1
    fi
}

download_dataset() {
    echo "💾 Downloading training data..."
    curl -sL "https://datasets.aicrowd.com/default/aicrowd-public-datasets/insurance-pricing-game/public/training.csv" > training.csv
    echo "✅ Downloaded training data"
}

download_magic_script() {
    curl -sL "https://gitlab.aicrowd.com/jyotish/pricing-game-notebook-scripts/raw/${BRANCH}/python/aicrowd_helpers.py" > aicrowd_helpers.py
}

download_prediction_script() {
    curl -sL "https://gitlab.aicrowd.com/jyotish/pricing-game-notebook-scripts/raw/${BRANCH}/python/predict.py" > ${SUBMISSION_DIR}/predict.py
}

prepare_submission_directory() {
    rm -rf ${SUBMISSION_DIR}
    mkdir -p ${SUBMISSION_DIR}
    execute_fn download_prediction_script
}

install_aicrowd_utilities() {
  echo "⚙️ Installing AIcrowd utilities..."
  pip install git+https://gitlab.aicrowd.com/yoogottamk/aicrowd-cli > /dev/null && mkdir -p ~/.config/aicrowd-cli && touch ~/.config/aicrowd-cli/config.toml
  echo "✅ Installed AIcrowd utilities"
}

execute_fn install_aicrowd_utilities
execute_fn download_magic_script
execute_fn prepare_submission_directory
#execute_fn download_dataset
