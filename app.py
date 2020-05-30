from psutil import process_iter
from signal import SIGTERM
import os
import time


def check_signer_alive(uinput):
    for proc in process_iter():
        for conns in proc.connections(kind='inet'):
            if conns.laddr.port == 55555:
                if uinput == "kill":
                    proc.send_signal(SIGTERM)
                    print("Signer proces uspješno ugašen.")
                elif uinput == "alivecheck":
                    print("Signer proces AKTIVAN.")


def find_signer_process_exe():
    signer = "Signer.exe"
    path_item = "middleware"
    different_paths = ["C:\Program Files", "C:\Program Files (x86)"]
    result = []
    for diff_path in different_paths:
        for root, dirs, files in os.walk(diff_path):
            if signer in files:
                result.append(os.path.join(root, signer))

    for res in result:
        if path_item.lower() in res.lower():
            signer_path = res
            return signer_path
        else:
            continue
    return False


def start_signer_app(signer_path):
    os.startfile(signer_path)


def main():
    check_signer_alive("kill")
    print("U potrazi za aplikacijom Signer.exe, molimo pričekajte...")
    if find_signer_process_exe():
        start_signer_app(find_signer_process_exe())
    else:
        print("Signer.exe ne postoji. Jeste li sigurni da je instaliran?")

    time.sleep(5)
    check_signer_alive("alivecheck")
    print("Slobodno ugasite eID Helper.")
    input()


if __name__ == '__main__':
    main()
