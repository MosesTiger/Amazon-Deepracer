def reward_function(params):
    reward=1e-3
    
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering = params['steering_angle']
    speed = params['speed']
    all_wheels_on_track = params['all_wheels_on_track']
    
    if distance_from_center >=0.0 and distance_from_center <=0.03:
        reward=1.0
    if not all_wheels_on_track:
        reward = reward-1
    else:
        reward = reward + (params['progress'])
        
    if speed < 2.68:
        reward *=0.80
    elif speed >=2.68 and speed <= 3.5:
        reward += speed
    else:
        reward = speed*speed+reward
    return float(reward)