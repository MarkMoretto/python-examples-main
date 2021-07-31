
import re
from pathlib import Path
from datetime import datetime as dt
import concurrent.futures as ccf

import requests

base_url = "https://www.science.smith.edu/~jcrouser/SDS293"

save_dir = Path(r"C:\Users\Work1\Desktop\Info\DataSciResources\SDS-293-ML")

LINK_PATTERN: str = r'href\s*=\s*"(lectures.+\.pdf)"'



class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = dt.now()

    @property
    def value(self):
        return (dt.now() - self.start_time).total_seconds()

    def peek(self):
        return self.value

    def finish(self):
        return self.value



def _clear_directory(p: Path, ignore_missing: bool = False):
    for f in p.glob("**/*"):
        p.joinpath(f).unlink(missing_ok = ignore_missing)


def _path_splitter(addr: str) -> str:
    return addr.split("/")[1]


def _url_maker(sub_address: str, base: str = base_url) -> str:
    return f"{base}/{sub_address}"


def get_and_save(subaddr: str, output_dir: Path = save_dir) -> None:

    output_filename: str = _path_splitter(subaddr)

    full_output_path: Path = output_dir.joinpath(output_filename)

    resp = requests.get(_url_maker(subaddr))
    if resp:
        full_output_path.write_bytes(resp.content)




def main():
    # Clear directory
    _clear_directory(save_dir, True)


    with requests.Session() as sess:

        data = sess.get(base_url).text

        if data:
            p = re.compile(LINK_PATTERN, flags=re.I | re.M)
            res = p.findall(data)

            if res:
                # urls = [f"{base_url}/{addr}" for addr in res]

                with ccf.ThreadPoolExecutor(max_workers = 10) as executor:
                    pdf_futures = {executor.submit(get_and_save, addr):addr for addr in res}
                    for future in ccf.as_completed(pdf_futures):
                        pdf_name = pdf_futures[future]
                        print(f"Completed processing: {pdf_name}")



if __name__ == "__main__":
    t = Timer()
    t.start()
    main()
    t.peek()
    res = t.finish()
    print(f"Processing took {res:}")

