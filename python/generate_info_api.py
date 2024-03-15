def info_data_to_json(txt_path):
    event_info = {"EventData" : {}}
    with open(txt_path, 'r') as file:
        lines = file.readlines()
    # 각 줄을 분석하여 JSON 형식으로 변환
    track_data = []
    for line in lines:
        parts = line.split()  # 공백으로 나누기
        if len(parts) < 9:  # 필요한 요소가 부족한 경우 건너뜀
            continue

        start_position = parts[:4]  # 시작 위치(마디)
        length = parts[-4:]  # 길이(마디)
        track = parts[-5]  # 트랙
        name = " ".join(parts[4:-5])  # 나머지 부분(이름)

        # Dictionary 형태로 데이터 저장
        track_info = {
            "Track": track,
            "Name": name,
            "StartPosition": start_position,
            "Length": length
        }

        track_data.append(track_info)

    # 결과 출력 (테스트용)
    for track in track_data:
        print(track)


info_data_to_json('aif_info/alaarmm.txt')
