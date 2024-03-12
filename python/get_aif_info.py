import subprocess
import modify_apple_script as mas

# AppleScript 파일 실행
def run_apple_script(apple_script_path):
    process = subprocess.run(["osascript", apple_script_path], text=True, capture_output=True)
    # subprocess.run() 함수를 사용하여 osascript 명령어 실행

    # 결과 출력 (디버그용)
    print("stdout:", process.stdout)
    print("stderr:", process.stderr)

    return process.stdout.strip()


#프로젝트 이름 가져오기 (ex. dingdong.logicx가 열려 있다면 "dingdong" 문자열 가져오기)
## applescript : 현재 logicx중 첫번째 process를 자동으로 가져옴 --> 나중에 원하는 logicx 파일 쓰도록 applescript 내용 변경 필요
def get_project_name():
    script_path = "applescripts/get_project_name.scpt"
    project_name = run_apple_script(script_path)
    return project_name.split(' - ')[0]


def get_project_info_aif():
    script = "applescripts/get_project_info_aif.applescript"
    project_name = get_project_name()
    txt_path = f"aif_info/{project_name}.txt"
    print(f"txt_path : {txt_path}")
    # print(txt_path.encode('iso-8859-1').decode('utf-8'))
    mas.modify_apple_script(script, "YOUR_TXT_PATH", txt_path)

    run_apple_script(script)

    mas.modify_apple_script(script, txt_path, "YOUR_TXT_PATH")


# 함수 호출
get_project_info_aif()
