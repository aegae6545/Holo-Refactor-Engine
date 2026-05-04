import asyncio
import sys
from agents.analyzer import ArchaeologistAgent
from agents.architect import ArchitectAgent
from agents.coder import ValidatorAgent
from config import Config

async def main():
    print("🚀 启动 Holo-Refactor-Engine v2.6...")
    print(f"⚙️ 配置模型: {Config.MIMO_MODEL} | 上下文窗口: {Config.MAX_CONTEXT_WINDOW}")
    
    # 模拟读取遗留代码
    legacy_code = "IDENTIFICATION DIVISION. PROGRAM-ID. BILLING..." * 100 
    
    # 初始化 Agent
    analyzer = ArchaeologistAgent()
    architect = ArchitectAgent()
    validator = ValidatorAgent()
    
    # 1. 分析阶段
    logic_report = await analyzer.run(legacy_code)
    
    # 2. 架构阶段
    design_doc = await architect.run(logic_report)
    
    # 3. 编码与验证阶段
    result = await validator.run(design_doc)
    
    print("\n✅ 任务完成！")
    print(result)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 任务已中止")