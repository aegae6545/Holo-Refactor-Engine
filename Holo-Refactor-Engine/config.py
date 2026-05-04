import os

class Config:
    # 模拟高配环境
    MIMO_MODEL = "mimo-1.5-pro" 
    MAX_CONTEXT_WINDOW = 1048576  # 1M Context
    TEMPERATURE = 0.2
    
    # 路径配置
    LEGACY_CODE_PATH = "./legacy_sample"
    OUTPUT_PATH = "./modernized_output"
    
    # API Keys (模拟)
    MIMO_API_KEY = os.getenv("MIMO_API_KEY", "sk-xxxxxxxxxxxx")