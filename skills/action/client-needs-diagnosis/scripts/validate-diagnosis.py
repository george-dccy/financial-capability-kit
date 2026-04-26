#!/usr/bin/env python3
"""
validate-diagnosis.py

校验客户需求诊断输出的完整性和合规性。
运行方式：python validate-diagnosis.py <output_file.md>
"""

import sys
import re

REQUIRED_FIELDS = [
    "需求类型判断",
    "信号依据",
    "置信度评估",
    "待验证项",
    "建议下一步",
]

RISK_PATTERNS = [
    (r"可以.*办理", "承诺办理"),
    (r"保证.*放款", "承诺放款"),
    (r"一定.*额度", "承诺额度"),
    (r"肯定.*批", "承诺审批"),
    (r".*授信.*没问题", "承诺授信"),
    (r"费率.*没问题", "承诺费率"),
]

def validate_diagnosis(content: str) -> dict:
    """Validate diagnosis output."""
    issues = []
    warnings = []

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in content:
            issues.append(f"缺少必需字段：{field}")

    # Check confidence level
    if "置信度" in content:
        confidence_match = re.search(r"置信度[：:]\s*(高|中|低)", content)
        if not confidence_match:
            warnings.append("置信度已提及但未标注具体等级（高/中/低）")
        else:
            confidence = confidence_match.group(1)
            # Low confidence should have clear verification items
            if confidence == "低" and "待验证项" in content:
                vt_section = re.search(r"待验证项[：:](.*?)(?=\n##|\n#|\Z)", content, re.DOTALL)
                if vt_section and len(vt_section.group(1).strip()) < 10:
                    warnings.append("置信度为低但待验证项内容过少")

    # Check risk patterns
    for pattern, risk_type in RISK_PATTERNS:
        if re.search(pattern, content):
            issues.append(f"检测到{risk_type}相关表述，需确认是否符合合规要求")

    # Check for customer sensitive info (basic check)
    sensitive_patterns = [
        r"\d{18}",  # ID number
        r"622202\d{13}",  # Bank card (partial)
    ]
    for pattern in sensitive_patterns:
        if re.search(pattern, content):
            issues.append("检测到疑似客户敏感信息，请确认已脱敏")

    # Check need type field has both level 1 and level 2
    if "需求类型判断" in content:
        need_type_section = re.search(r"需求类型判断[：:](.*?)(?=\n##|\n#|\Z)", content, re.DOTALL)
        if need_type_section:
            need_type_text = need_type_section.group(1)
            # Should have some content
            if len(need_type_text.strip()) < 5:
                issues.append("需求类型判断内容过少")

    return {
        "valid": len(issues) == 0,
        "issues": issues,
        "warnings": warnings,
    }

def main():
    if len(sys.argv) < 2:
        print("用法: python validate-diagnosis.py <output_file.md>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"错误：文件不存在 {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"错误：读取文件失败 {e}")
        sys.exit(1)

    result = validate_diagnosis(content)

    print("=" * 50)
    print("诊断输出校验结果")
    print("=" * 50)

    if result["valid"]:
        print("✓ 校验通过")
    else:
        print("✗ 校验失败")
        for issue in result["issues"]:
            print(f"  - {issue}")

    if result["warnings"]:
        print("\n⚠ 警告")
        for warning in result["warnings"]:
            print(f"  - {warning}")

    sys.exit(0 if result["valid"] else 1)

if __name__ == "__main__":
    main()
