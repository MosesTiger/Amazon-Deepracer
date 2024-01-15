import math

def reward_function(params):
    # 입력 변수들을 읽어옵니다.
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    speed = params['speed']
    steering = params['steering_angle']
    all_wheels_on_track = params['all_wheels_on_track']
    progress = params['progress']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']

    # 기본 보상 값을 설정합니다.
    reward = 1.0

    # 트랙 방향 계산
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    track_direction = math.degrees(track_direction)

    # 트랙 방향과 헤딩 간 차이 계산
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # 방향 차이가 크면 보상 감소
    DIRECTION_THRESHOLD = 10.0
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5

    # 속도에 따른 보상
    SPEED_THRESHOLD = 1.5
    if speed > SPEED_THRESHOLD:
        reward *= 1.2

    # 스티어링 각도에 따른 보상
    STEERING_THRESHOLD = 20.0
    if abs(steering) < STEERING_THRESHOLD:
        reward *= 1.1

    # 트랙 중앙 유지 보상
    if distance_from_center < 0.5 * track_width:
        reward *=1.3

    # 진행도에 따른 보상
    reward += progress / 100

    # 전체 바퀴가 트랙에 있을 때의 보상
    if all_wheels_on_track:
        reward *=1.2

    return float(reward)