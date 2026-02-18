# Disease Information Database

DISEASE_INFO = {
    # Pepper Classes
    "Pepper__bell___Bacterial_spot": {
        "name": "Pepper Bell Bacterial Spot",
        "description": "Bacterial spot is caused by Xanthomonas bacteria. It appears as dark, water-soaked spots on leaves, stems, and fruits.",
        "treatments": {
            "chemical": ["Copper-based bactericides", "Mancozeb fungicide"],
            "organic": ["Neem oil spray", "Copper soap fungicide", "Remove infected parts"]
        },
        "medicines": ["Kocide 3000", "Champion WP", "Neem Oil 1500 ppm"]
    },
    "Pepper__bell___healthy": {
        "name": "Healthy Pepper Plant",
        "description": "Your pepper plant is thriving! Maintain regular watering and check for signs of pests periodically.",
        "treatments": {
            "chemical": ["No chemical treatment needed"],
            "organic": ["Balanced organic fertilizer", "Regular mulching"]
        },
        "medicines": ["Organic Growth Booster (Optional)"]
    },

    # Potato Classes
    "Potato___Early_blight": {
        "name": "Potato Early Blight",
        "description": "Fungal disease caused by Alternaria solani, creating target-like spots on leaves.",
        "treatments": {
            "chemical": ["Chlorothalonil", "Mancozeb", "Azoxystrobin"],
            "organic": ["Neem oil", "Copper organic fungicides", "Crop rotation"]
        },
        "medicines": ["Mancozeb 75% WP", "Chlorothalonil 75% WP"]
    },
    "Potato___Late_blight": {
        "name": "Potato Late Blight",
        "description": "Devastating fungal disease caused by Phytophthora infestans. Can destroy crops rapidly in humid conditions.",
        "treatments": {
            "chemical": ["Metalaxyl + Mancozeb", "Chlorothalonil"],
            "organic": ["Copper-based sprays", "Immediate removal of infected plants"]
        },
        "medicines": ["Ridomil Gold", "Bordeaux mixture"]
    },
    "Potato___healthy": {
        "name": "Healthy Potato Plant",
        "description": "Your potatoes look great. Keep an eye on soil moisture and ensure good hilling for tuber protection.",
        "treatments": {
            "chemical": ["No treatment required"],
            "organic": ["Compost tea", "Balanced nutrition"]
        },
        "medicines": ["None needed"]
    },

    # Tomato Classes
    "Tomato_Bacterial_spot": {
        "name": "Tomato Bacterial Spot",
        "description": "Bacterial disease causing dark spots and fruit lesions. Thrives in warm, wet weather.",
        "treatments": {
            "chemical": ["Copper Oxychloride", "Streptocycline"],
            "organic": ["Copper soap", "Neem oil", "Improved air circulation"]
        },
        "medicines": ["Streptocycline", "Kocide"]
    },
    "Tomato_Early_blight": {
        "name": "Tomato Early Blight",
        "description": "Common fungal disease causing target-spots on lower leaves first.",
        "treatments": {
            "chemical": ["Mancozeb", "Chlorothalonil"],
            "organic": ["Mulching", "Pruning lower leaves", "Neem oil"]
        },
        "medicines": ["Mancozeb", "Chlorothalonil"]
    },
    "Tomato_Late_blight": {
        "name": "Tomato Late Blight",
        "description": "Highly contagious fungal-like disease. Causes dark water-soaked spots on leaves and fruit.",
        "treatments": {
            "chemical": ["Ridomil Gold", "Metalaxyl"],
            "organic": ["Copper sprays", "Total destruction of infected plants"]
        },
        "medicines": ["Ridomil Gold", "Champion"]
    },
    "Tomato_Leaf_Mold": {
        "name": "Tomato Leaf Mold",
        "description": "Fungal disease common in high humidity. Causes fuzzy growth on leaf undersides.",
        "treatments": {
            "chemical": ["Chlorothalonil", "Mancozeb"],
            "organic": ["Reduce humidity", "Proper ventilation", "Neem oil"]
        },
        "medicines": ["Mancozeb", "Sulfur-based fungicides"]
    },
    "Tomato_Septoria_leaf_spot": {
        "name": "Tomato Septoria Leaf Spot",
        "description": "One of the most destructive diseases of tomato foliage. Causes small, circular spots with dark borders.",
        "treatments": {
            "chemical": ["Chlorothalonil", "Copper-based fungicides"],
            "organic": ["Avoid overhead watering", "Prune lower branches", "Mulch"]
        },
        "medicines": ["Daconil (Chlorothalonil)", "Copper Fungicide"]
    },
    "Tomato_healthy": {
        "name": "Healthy Tomato Plant",
        "description": "Your tomato plant is healthy and productive. Continue with regular staking and pruning for best yields.",
        "treatments": {
            "chemical": ["None required"],
            "organic": ["Liquid seaweed fertilizer", "Balanced watering"]
        },
        "medicines": ["Fish Emulsion (Optional)"]
    },

    "default": {
        "name": "Condition Recognized",
        "description": "We've detected a condition, but specific local recommendations may apply. Please consult an expert.",
        "treatments": {
            "chemical": ["Consult local agricultural specialist"],
            "organic": ["General neem oil application", "Remove suspicious leaves"]
        },
        "medicines": ["Broad spectrum products"]
    }
}

def get_disease_info(disease_name):
    """Get disease information by name with fuzzy mapping"""
    # Try exact match first
    if disease_name in DISEASE_INFO:
        return DISEASE_INFO[disease_name]
    
    # Try normalized match (replacing spaces with underscores)
    normalized = disease_name.replace(' ', '_')
    if normalized in DISEASE_INFO:
        return DISEASE_INFO[normalized]
    
    # Fallback to default
    return DISEASE_INFO['default']
