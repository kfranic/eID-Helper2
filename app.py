from psutil import process_iter
from signal import SIGTERM
import os


def check_signer_alive(uinput):
    for proc in process_iter():
        for conns in proc.connections(kind='inet'):
            if conns.laddr.port == 55555:
                if uinput == "kill":
                    proc.send_signal(SIGTERM)
                    print("Signer proces uspješno ugašen.")
                else:
                    print("Signer proces AKTIVAN.")


def find_signer_process_exe():
    print("U potrazi za aplikacijom Signer.exe, molimo pričekajte...")
    name = "winvnc.exe"
    path_item = "ultravnc"
    different_paths = ["C:\Program Files", "C:\Program Files (x86)"]
    result = []
    for diff_path in different_paths:
        for root, dirs, files in os.walk(diff_path):
            if name in files:
                result.append(os.path.join(root, name))

    for res in result:
        if path_item.lower() in res.lower():
            signer_path = res
            print(f"Signer.exe pronađen: {signer_path}")
            return signer_path
        else:
            continue
    return False


def start_signer_app(signer_path):
    os.startfile(signer_path)


def main():
    check_signer_alive("kill")
    start_signer_app(find_signer_process_exe())
    check_signer_alive("alive_check")
    input()

if __name__ == '__main__':
    main()


