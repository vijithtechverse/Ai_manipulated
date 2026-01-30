def final_decision(metadata_flag, ela_score, noise_var, model_pred):
    score = 0

    if metadata_flag:
        score += 1
    if ela_score > 15:
        score += 1
    if noise_var < 100:
        score += 1
    if model_pred == 1:
        score += 2

    if score >= 3:
        return "AI Manipulated", score
    else:
        return "Real Image", score
