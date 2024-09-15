def draw_pose_angles(image, results, joint_list):
    cnt = 0
    temp_arr = []
    for pose_landmarks in results.pose_landmarks:
        # Loop through joint sets
        for joint in joint_list:
            a = np.array([pose_landmarks.landmark[joint[0]].x, pose_landmarks.landmark[joint[0]].y]) # First coord
            b = np.array([pose_landmarks.landmark[joint[1]].x, pose_landmarks.landmark[joint[1]].y]) # Second coord
            c = np.array([pose_landmarks.landmark[joint[2]].x, pose_landmarks.landmark[joint[2]].y]) # Third coord

            radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
            angle = np.abs(radians * 180.0 / np.pi)

            if angle > 180.0:
                angle = 360 - angle
            angle = 180 - angle
            angle = str(round(angle, 2))
            temp_arr.append(angle)
            cv2.putText(image, angle, tuple(np.multiply(b, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cnt += 1
        print(temp_arr)
    return image