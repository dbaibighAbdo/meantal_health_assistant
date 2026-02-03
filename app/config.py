"""
Configuration file for Mental Health Chatbot
Modify these settings to customize the chatbot behavior
"""

# ============================================================================
# MODEL CONFIGURATION
# ============================================================================

# Hugging Face model IDs
CHAT_MODEL_ID = "dbaibighAbdo/mental_health_finetuned_qwen2.5_3b_instruct"
CLASSIFICATION_MODEL_ID = "dbaibighAbdo/mental_health_robertaL_tc"

# Model loading settings
MODEL_CONFIG = {
    "torch_dtype": "bfloat16",  # Options: "bfloat16", "float16", "float32"
    "device_map": "auto",        # Options: "auto", "cpu", "cuda:0"
    "low_cpu_mem_usage": True,
    "offload_folder": "./offload_dir"  # For CPU offloading
}

# ============================================================================
# GENERATION PARAMETERS
# ============================================================================

GENERATION_CONFIG = {
    "max_new_tokens": 256,      # Maximum length of generated response
    "temperature": 0.7,         # Creativity level (0.0 = deterministic, 1.0 = very creative)
    "top_p": 0.9,              # Nucleus sampling threshold
    "top_k": 50,               # Top-k sampling
    "do_sample": True,         # Enable sampling (vs greedy)
    "repetition_penalty": 1.1, # Penalty for repeating tokens
    "num_beams": 1,            # Beam search (1 = no beam search)
}

# ============================================================================
# EMOTION CONFIGURATION
# ============================================================================

# Emotion categories and their properties
EMOTIONS = {
    "suicidal": {
        "severity": "critical",
        "color": "#dc3545",
        "requires_resources": True
    },
    "depression": {
        "severity": "high",
        "color": "#6c757d",
        "requires_resources": False
    },
    "anxiety": {
        "severity": "high",
        "color": "#ffc107",
        "requires_resources": False
    },
    "stress": {
        "severity": "medium",
        "color": "#fd7e14",
        "requires_resources": False
    },
    "bipolar": {
        "severity": "high",
        "color": "#6f42c1",
        "requires_resources": False
    },
    "personality disorder": {
        "severity": "medium",
        "color": "#e83e8c",
        "requires_resources": False
    },
    "normal": {
        "severity": "low",
        "color": "#28a745",
        "requires_resources": False
    },
    "neutral": {
        "severity": "low",
        "color": "#17a2b8",
        "requires_resources": False
    }
}

# Crisis keywords that trigger immediate response
CRISIS_KEYWORDS = [
    "suicide", "kill myself", "end it all", "no reason to live",
    "want to die", "better off dead", "end my life"
]

# Greeting keywords
GREETING_KEYWORDS = [
    "hi", "hello", "hey", "good morning", "good evening",
    "greetings", "howdy", "hi there", "hello there"
]

# ============================================================================
# SYSTEM PROMPTS
# ============================================================================

SYSTEM_PROMPTS = {
    "crisis": """You are a compassionate mental health crisis counselor. 
    The user may be in distress. Respond with immediate empathy, 
    validate their feelings, and gently encourage them to seek 
    professional help. Be calm, supportive, and non-judgmental.""",
    
    "greeting": """You are a warm and welcoming mental health assistant. 
    Greet the user kindly and invite them to share what's on their mind. 
    Keep your response brief and friendly.""",
    
    "suicidal": """You are an empathetic crisis counselor. The user is 
    expressing suicidal thoughts. Respond with deep compassion, validate 
    their pain, and encourage professional help.""",
    
    "depression": """You are a supportive mental health assistant. 
    The user may be experiencing depression. Respond with empathy, 
    acknowledge their feelings, and offer gentle encouragement.""",
    
    "anxiety": """You are a calming mental health assistant. The user 
    may be experiencing anxiety. Respond with reassurance, help them 
    feel grounded, and offer supportive guidance.""",
    
    "stress": """You are a supportive mental health assistant. The user 
    is experiencing stress. Respond with understanding and practical 
    emotional support.""",
    
    "bipolar": """You are an understanding mental health assistant. 
    Respond with stability, empathy, and encourage healthy coping strategies.""",
    
    "personality disorder": """You are a non-judgmental mental health 
    assistant. Respond with empathy and encourage professional support.""",
    
    "default": """You are a friendly and supportive mental health assistant. 
    Respond naturally, show genuine interest, and create a safe 
    space for conversation."""
}

# ============================================================================
# CRISIS RESOURCES
# ============================================================================

CRISIS_RESOURCES = {
    "US": {
        "Suicide Prevention Lifeline": "988",
        "Crisis Text Line": "Text HOME to 741741",
        "SAMHSA Helpline": "1-800-662-4357"
    },
    "International": {
        "IASP Crisis Centers": "https://www.iasp.info/resources/Crisis_Centres/",
        "Befrienders Worldwide": "https://www.befrienders.org/"
    }
}

CRISIS_MESSAGE = """

⚠️ If you're in crisis, please reach out immediately:
• National Suicide Prevention Lifeline: 988 (US)
• Crisis Text Line: Text HOME to 741741
• International Association for Suicide Prevention: https://www.iasp.info/resources/Crisis_Centres/
"""

# ============================================================================
# UI CONFIGURATION
# ============================================================================

UI_CONFIG = {
    "page_title": "Mental Health Support Chatbot",
    "page_icon": "🧠",
    "layout": "wide",
    "theme": {
        "primaryColor": "#1f77b4",
        "backgroundColor": "#ffffff",
        "secondaryBackgroundColor": "#f0f2f6",
        "textColor": "#262730"
    }
}

# Quick prompt options
QUICK_PROMPTS = [
    ("😊", "I'm feeling good today"),
    ("😰", "I'm feeling anxious"),
    ("😔", "I'm feeling down"),
    ("💭", "I need someone to talk to"),
    ("😤", "I'm feeling stressed"),
    ("😌", "I want to talk about my day")
]

# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================

LOGGING_CONFIG = {
    "level": "INFO",  # Options: "DEBUG", "INFO", "WARNING", "ERROR"
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "log_to_file": False,
    "log_file": "chatbot.log"
}

# ============================================================================
# SESSION CONFIGURATION
# ============================================================================

SESSION_CONFIG = {
    "enable_memory": True,           # Enable conversation memory
    "max_history_length": 50,        # Maximum messages to keep in history
    "session_timeout_minutes": 60,   # Session timeout
    "auto_save_interval": 5          # Auto-save every N messages
}

# ============================================================================
# ANALYTICS CONFIGURATION
# ============================================================================

ANALYTICS_CONFIG = {
    "enable_emotion_tracking": True,
    "enable_confidence_tracking": True,
    "emotion_chart_height": 300,
    "show_statistics": True,
    "export_format": "json"  # Options: "json", "csv"
}