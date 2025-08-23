def generate_score_report(names: list[str], scores: list[int]):
    report = []
    for name, score in zip(names, scores):
        report.append(f"{name} scored {score} marks")
    return report
