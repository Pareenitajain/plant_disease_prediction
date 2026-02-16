# Disease Information Database

DISEASE_INFO = {
    "Pepper__bell___Bacterial_spot": {
        "name": "Pepper Bell Bacterial Spot",
        "description": "Bacterial spot is a common disease affecting pepper plants, caused by Xanthomonas bacteria. It appears as dark, water-soaked spots on leaves, stems, and fruits.",
        "symptoms": [
            "Small, dark brown spots on leaves",
            "Water-soaked lesions on fruits",
            "Yellow halos around spots",
            "Leaf drop in severe cases",
            "Reduced fruit quality and yield"
        ],
        "treatments": {
            "chemical": [
                "Copper-based bactericides (Copper hydroxide, Copper sulfate)",
                "Mancozeb fungicide",
                "Streptomycin sulfate (where permitted)"
            ],
            "organic": [
                "Neem oil spray",
                "Copper soap fungicide",
                "Bacillus subtilis biological control",
                "Remove and destroy infected plant parts"
            ]
        },
        "prevention": [
            "Use disease-free seeds and transplants",
            "Rotate crops annually",
            "Avoid overhead watering",
            "Maintain proper plant spacing for air circulation",
            "Disinfect tools between plants"
        ],
        "medicines": [
            "Kocide 3000 (Copper Hydroxide)",
            "Champion WP (Copper Hydroxide)",
            "Mancozeb 75% WP",
            "Neem Oil 1500 ppm"
        ]
    },
    "Tomato___Bacterial_spot": {
        "name": "Tomato Bacterial Spot",
        "description": "A bacterial disease affecting tomato plants, causing leaf spots and fruit lesions that reduce crop quality and yield.",
        "symptoms": [
            "Small dark spots with yellow halos on leaves",
            "Raised spots on fruits",
            "Leaf yellowing and defoliation",
            "Stunted plant growth"
        ],
        "treatments": {
            "chemical": [
                "Copper-based sprays",
                "Streptomycin (if available)",
                "Mancozeb fungicide"
            ],
            "organic": [
                "Copper soap",
                "Neem oil",
                "Remove infected leaves",
                "Improve air circulation"
            ]
        },
        "prevention": [
            "Use certified disease-free seeds",
            "Practice crop rotation",
            "Avoid working with wet plants",
            "Use drip irrigation instead of overhead watering"
        ],
        "medicines": [
            "Copper Oxychloride 50% WP",
            "Streptocycline",
            "Bordeaux mixture",
            "Neem-based products"
        ]
    },
    "Potato___Early_blight": {
        "name": "Potato Early Blight",
        "description": "Fungal disease caused by Alternaria solani, creating characteristic target-like spots on leaves and reducing tuber quality.",
        "symptoms": [
            "Brown spots with concentric rings (target pattern)",
            "Lower leaves affected first",
            "Yellowing around spots",
            "Premature leaf drop",
            "Reduced tuber size"
        ],
        "treatments": {
            "chemical": [
                "Chlorothalonil fungicide",
                "Mancozeb",
                "Azoxystrobin",
                "Copper fungicides"
            ],
            "organic": [
                "Neem oil spray",
                "Copper-based organic fungicides",
                "Remove infected plant debris",
                "Mulching to prevent soil splash"
            ]
        },
        "prevention": [
            "Plant resistant varieties",
            "Rotate crops (3-4 year cycle)",
            "Maintain proper plant nutrition",
            "Remove plant debris after harvest",
            "Ensure good air circulation"
        ],
        "medicines": [
            "Mancozeb 75% WP",
            "Chlorothalonil 75% WP",
            "Azoxystrobin 23% SC",
            "Copper Oxychloride"
        ]
    },
    "Tomato___Late_blight": {
        "name": "Tomato Late Blight",
        "description": "Devastating fungal disease caused by Phytophthora infestans, can destroy entire crops within days in favorable conditions.",
        "symptoms": [
            "Water-soaked spots on leaves",
            "White fuzzy growth on leaf undersides",
            "Brown lesions on stems",
            "Firm brown spots on fruits",
            "Rapid plant collapse"
        ],
        "treatments": {
            "chemical": [
                "Metalaxyl + Mancozeb",
                "Chlorothalonil",
                "Copper fungicides",
                "Cymoxanil + Mancozeb"
            ],
            "organic": [
                "Copper-based sprays",
                "Remove and destroy infected plants immediately",
                "Improve drainage",
                "Reduce humidity"
            ]
        },
        "prevention": [
            "Use resistant varieties",
            "Avoid overhead irrigation",
            "Provide adequate spacing",
            "Remove volunteer plants",
            "Monitor weather conditions"
        ],
        "medicines": [
            "Ridomil Gold (Metalaxyl + Mancozeb)",
            "Curzate (Cymoxanil)",
            "Bordeaux mixture",
            "Copper Hydroxide"
        ]
    },
    "Tomato___Leaf_Mold": {
        "name": "Tomato Leaf Mold",
        "description": "Fungal disease common in greenhouse tomatoes, caused by Passalora fulva, thriving in high humidity.",
        "symptoms": [
            "Pale green or yellow spots on upper leaf surface",
            "Olive-green to brown fuzzy growth underneath",
            "Leaves curl and die",
            "Reduced photosynthesis",
            "Lower leaves affected first"
        ],
        "treatments": {
            "chemical": [
                "Chlorothalonil",
                "Mancozeb",
                "Copper fungicides"
            ],
            "organic": [
                "Improve ventilation",
                "Reduce humidity",
                "Remove infected leaves",
                "Neem oil spray"
            ]
        },
        "prevention": [
            "Maintain humidity below 85%",
            "Ensure good air circulation",
            "Avoid overhead watering",
            "Space plants properly",
            "Use resistant varieties"
        ],
        "medicines": [
            "Mancozeb 75% WP",
            "Chlorothalonil 75% WP",
            "Copper Oxychloride",
            "Sulfur-based fungicides"
        ]
    },
    "default": {
        "name": "Plant Disease",
        "description": "A plant disease has been detected. Please consult with a local agricultural expert for specific treatment recommendations.",
        "symptoms": [
            "Visible abnormalities on plant",
            "Discoloration or spots",
            "Wilting or stunted growth"
        ],
        "treatments": {
            "chemical": [
                "Consult local agricultural extension office",
                "Use broad-spectrum fungicide as preventive measure"
            ],
            "organic": [
                "Neem oil spray",
                "Remove affected plant parts",
                "Improve plant health through proper nutrition"
            ]
        },
        "prevention": [
            "Maintain plant health",
            "Ensure proper watering",
            "Provide adequate nutrition",
            "Monitor plants regularly"
        ],
        "medicines": [
            "General purpose fungicide",
            "Neem-based products",
            "Copper-based fungicides"
        ]
    }
}

def get_disease_info(disease_name):
    """Get disease information by name"""
    # Normalize disease name
    disease_key = disease_name.replace(' ', '_')
    
    # Return specific info or default
    return DISEASE_INFO.get(disease_key, DISEASE_INFO['default'])
