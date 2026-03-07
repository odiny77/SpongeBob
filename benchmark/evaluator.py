from typing import Any, Dict


def run_benchmark(model, tokenizer, c3_path: str, xcopa_path: str) -> Dict[str, Any]:
    """
    占位版 benchmark 评测函数。

    真实项目中，你可以在这里加载 C3 / XCOPA 等数据集，
    调用模型生成或分类，并计算准确率、loss 等指标。

    当前实现只返回一个固定字典，用于保证训练脚本能够正常运行和记录。
    """
    # 为了兼容 swanlab.log(eval_results, step=...)，返回一个 dict
    return {
        "c3_accuracy": 0.0,
        "xcopa_accuracy": 0.0,
        "note": "Placeholder benchmark. Please implement real evaluation in benchmark/evaluator.py.",
    }

