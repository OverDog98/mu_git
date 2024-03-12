from pathlib import Path
import binascii


def read_project_data():
    # 파일 경로 설정
    project_data_path = Path(
        "/Users/sangjin/Desktop/ProjectData")

    # 파일이 존재하는지 확인
    if project_data_path.exists():
        # 파일을 바이너리 모드로 열고 내용을 읽은 후, 16진수 형태로 인코딩
        with project_data_path.open('rb') as file:
            data = file.read()
            hex_data = binascii.hexlify(data).decode('ascii')

            # 결과 출력 (처음 1000자만)
            print(hex_data[:1000])
    else:
        print("ProjectData 파일을 찾을 수 없습니다.")


# 함수 실행
read_project_data()
