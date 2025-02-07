import re
import argparse
from eyepop import EyePopSdk
from config import pop_id, secret_key
from collections import defaultdict


parser = argparse.ArgumentParser(description='Extract and structure data from an image.')
parser.add_argument('filename', type=str, help='The path to the image file')
args = parser.parse_args()

with EyePopSdk.workerEndpoint(pop_id=pop_id, secret_key=secret_key) as endpoint:
    result = endpoint.upload(args.filename).predict()
    

# result = {'objects': [{'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.9387, 'height': 20.237, 'id': 97, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9958, 'id': 192, 'text': '(21g)'}], 'width': 51.443, 'x': 241.097, 'y': 78.604}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.936, 'height': 15.842, 'id': 98, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9958, 'id': 191, 'text': 'Sugars'}], 'width': 47.583, 'x': 64.524, 'y': 349.737}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.9339, 'height': 17.904, 'id': 99, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9972, 'id': 190, 'text': 'container'}], 'width': 77.727, 'x': 136.694, 'y': 59.013}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.9285, 'height': 18.171, 'id': 100, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9945, 'id': 189, 'text': 'servings'}], 'width': 68.587, 'x': 35.485, 'y': 60.403}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.9231, 'height': 30.671, 'id': 101, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9998, 'id': 188, 'text': '60'}], 'width': 52.59, 'x': 239.148, 'y': 130.703}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.9135, 'height': 17.228, 'id': 102, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9997, 'id': 187, 'text': '16'}], 'width': 21.756, 'x': 10.433, 'y': 58.541}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.9028, 'height': 16.068, 'id': 103, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9897, 'id': 186, 'text': 'Sodium'}], 'width': 64.687, 'x': 9.038, 'y': 284.445}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.9025, 'height': 16.307, 'id': 104, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9979, 'id': 185, 'text': 'size'}], 'width': 41.012, 'x': 88.02, 'y': 79.273}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.9003, 'height': 15.518, 'id': 105, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9959, 'id': 184, 'text': 'Vitamin'}], 'width': 50.595, 'x': 8.993, 'y': 425.826}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.8854, 'height': 15.593, 'id': 106, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9982, 'id': 183, 'text': 'Total'}], 'width': 44.256, 'x': 9.349, 'y': 305.846}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.8808, 'height': 16.538, 'id': 107, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9277, 'id': 182, 'text': '0mg'}], 'width': 30.113, 'x': 38.603, 'y': 469.936}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.8743, 'height': 15.342, 'id': 108, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9927, 'id': 181, 'text': 'Protein'}], 'width': 60.323, 'x': 10.05, 'y': 391.97}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.8742, 'height': 15.403, 'id': 109, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9981, 'id': 180, 'text': 'Total'}], 'width': 44.491, 'x': 9.566, 'y': 198.871}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.872, 'height': 31.828, 'id': 110, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9962, 'id': 179, 'text': 'Nutrition'}], 'width': 167.207, 'x': 8.382, 'y': 20.149}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.866, 'height': 18.253, 'id': 111, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9625, 'id': 178, 'text': 'Tbsp.'}], 'width': 57.284, 'x': 180.344, 'y': 79.724}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.8659, 'height': 16.502, 'id': 112, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9448, 'id': 177, 'text': '0g'}], 'width': 17.335, 'x': 114.351, 'y': 329.036}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.8584, 'height': 16.513, 'id': 113, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9961, 'id': 176, 'text': 'Trans'}], 'width': 39.364, 'x': 28.424, 'y': 242.035}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.8554, 'height': 15.539, 'id': 114, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9981, 'id': 175, 'text': '17g'}], 'width': 26.455, 'x': 113.308, 'y': 349.577}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.852, 'height': 16.126, 'id': 115, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9967, 'id': 174, 'text': 'Fiber'}], 'width': 34.626, 'x': 77.826, 'y': 327.77}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.8503, 'height': 17.738, 'id': 116, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9951, 'id': 173, 'text': 'Serving'}], 'width': 75.018, 'x': 8.888, 'y': 79.833}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.8458, 'height': 15.453, 'id': 117, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9255, 'id': 172, 'text': '0g'}], 'width': 17.93, 'x': 71.381, 'y': 393.207}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.8406, 'height': 17.772, 'id': 118, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9947, 'id': 171, 'text': 'Carbohydrate'}], 'width': 103.009, 'x': 58.575, 'y': 305.008}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.8381, 'height': 16.488, 'id': 119, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.7995, 'id': 170, 'text': '0mg'}], 'width': 30.93, 'x': 72.445, 'y': 285.339}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.8333, 'height': 30.582, 'id': 120, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9982, 'id': 169, 'text': 'Facts'}], 'width': 105.446, 'x': 188.056, 'y': 20.588}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.828, 'height': 16.045, 'id': 121, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9988, 'id': 168, 'text': '17g'}], 'width': 25.352, 'x': 166.571, 'y': 306.348}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.8129, 'height': 15.707, 'id': 122, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9422, 'id': 167, 'text': '0g'}], 'width': 18.007, 'x': 93.23, 'y': 242.91}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.8028, 'height': 15.138, 'id': 123, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9982, 'id': 166, 'text': '0%'}], 'width': 27.436, 'x': 264.388, 'y': 199.08}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.8009, 'height': 15.569, 'id': 124, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.956, 'id': 165, 'text': '0g'}], 'width': 18.295, 'x': 85.229, 'y': 199.731}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.7999, 'height': 15.554, 'id': 125, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9976, 'id': 164, 'text': 'Fat'}], 'width': 25.025, 'x': 68.312, 'y': 241.953}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.7996, 'height': 16.067, 'id': 126, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9982, 'id': 163, 'text': '1'}], 'width': 11.256, 'x': 164.685, 'y': 80.082}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.7946, 'height': 15.388, 'id': 127, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.7845, 'id': 162, 'text': '0mg'}], 'width': 30.302, 'x': 104.46, 'y': 264.428}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.7889, 'height': 15.634, 'id': 128, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9716, 'id': 161, 'text': 'Potassium'}], 'width': 72.13, 'x': 7.857, 'y': 489.996}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.7883, 'height': 15.392, 'id': 129, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9606, 'id': 160, 'text': '0g'}], 'width': 17.888, 'x': 118.909, 'y': 222.623}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.779, 'height': 15.153, 'id': 130, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9988, 'id': 159, 'text': '0%'}], 'width': 24.642, 'x': 267.058, 'y': 426.642}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.7778, 'height': 15.166, 'id': 131, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.8077, 'id': 158, 'text': '0mg'}], 'width': 30.261, 'x': 80.411, 'y': 491.077}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.7759, 'height': 25.764, 'id': 132, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9938, 'id': 157, 'text': 'Calories'}], 'width': 128.817, 'x': 12.293, 'y': 136.064}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.773, 'height': 15.15, 'id': 133, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.8362, 'id': 156, 'text': '0mg'}], 'width': 29.784, 'x': 66.284, 'y': 447.866}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.7681, 'height': 15.56, 'id': 134, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9989, 'id': 155, 'text': 'D'}], 'width': 13.293, 'x': 61.45, 'y': 425.928}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.7606, 'height': 15.897, 'id': 135, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.6538, 'id': 154, 'text': 'Omcg'}], 'width': 37.05, 'x': 75.848, 'y': 426.675}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.7542, 'height': 15.921, 'id': 136, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9977, 'id': 153, 'text': 'Dietary'}], 'width': 45.535, 'x': 29.346, 'y': 327.82}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.7496, 'height': 15.455, 'id': 137, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9988, 'id': 152, 'text': '0%'}], 'width': 24.689, 'x': 267.181, 'y': 469.446}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.7337, 'height': 15.15, 'id': 138, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.5732, 'id': 151, 'text': '34%1'}], 'width': 42.213, 'x': 249.438, 'y': 370.996}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.7293, 'height': 15.272, 'id': 139, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9927, 'id': 150, 'text': 'Calcium'}], 'width': 53.947, 'x': 9.765, 'y': 446.776}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.729, 'height': 15.249, 'id': 140, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9986, 'id': 149, 'text': 'Fat'}], 'width': 28.252, 'x': 55.459, 'y': 199.319}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.7176, 'height': 15.785, 'id': 141, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9983, 'id': 148, 'text': 'Total'}], 'width': 35.459, 'x': 26.494, 'y': 348.058}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.7067, 'height': 14.786, 'id': 142, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9983, 'id': 147, 'text': 'Fat'}], 'width': 22.888, 'x': 94.829, 'y': 221.317}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.7043, 'height': 15.219, 'id': 143, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9987, 'id': 146, 'text': '0%'}], 'width': 27.565, 'x': 264.279, 'y': 263.184}, {'category': 'text', 'classId': 0, 'classLabel': 'text', 'confidence': 0.7011, 'height': 15.231, 'id': 144, 'orientation': 0, 'texts': [{'category': 'text', 'confidence': 0.9983, 'id': 145, 'text': '0%'}], 'width': 24.164, 'x': 267.352, 'y': 446.997}], 'seconds': 0, 'source_height': 600, 'source_id': 'abc576bf-e34b-11ef-9fb3-0242ac110007', 'source_width': 300, 'system_timestamp': 1738709962619023000, 'timestamp': 0}

# Example response (truncated for brevity)
# response = {
#     'objects': [
#         {
#             'category': 'text',
#             'classId': 0,
#             'classLabel': 'text',
#             'confidence': 0.9387,
#             'height': 20.237,
#             'id': 97,
#             'orientation': 0,
#             'texts': [{'category': 'text', 'confidence': 0.9958, 'id': 192, 'text': '(21g)'}],
#             'width': 51.443,
#             'x': 241.097,
#             'y': 78.604
#         },
#         # ... other objects ...
#     ],
#     'seconds': 0,
#     'source_height': 600,
#     'source_id': 'abc576bf-e34b-11ef-9fb3-0242ac110007',
#     'source_width': 300,
#     'system_timestamp': 1738709962619023000,
#     'timestamp': 0
# }

# Define a template for the nutrition data object
nutrition_data_template = {
    "calories": None,
    "totalFat": None,
    "saturatedFat": None,
    "transFat": None,
    "cholesterol": None,
    "sodium": None,
    "totalCarbohydrate": None,
    "dietaryFiber": None,
    "sugars": None,
    "protein": None,
    "vitaminA": None,
    "vitaminC": None,
    "calcium": None,
    "iron": None,
    "vitaminD": None,
    "potassium": None,
    "servingSize": None,
    "servingsPerContainer": None
}

# Sort the objects by their 'y' field to process them in order from top to bottom
sorted_objects = sorted(result['objects'], key=lambda x: x['y'])

# Group the objects by their 'y' value within a range of 10 units to handle lines of text
grouped_by_y = defaultdict(list)
current_group_y = None

for obj in sorted_objects:
    if current_group_y is None or abs(obj['y'] - current_group_y) > 10:
        current_group_y = obj['y']
    grouped_by_y[current_group_y].append(obj)

# Sort within each group by 'x' value to process text from left to right
associated_texts = []
for y_value in sorted(grouped_by_y.keys()):
    group = grouped_by_y[y_value]
    sorted_group = sorted(group, key=lambda x: x['x'])
    texts = [obj['texts'][0]['text'] for obj in sorted_group if 'texts' in obj and obj['texts']]
    filtered_texts = [text for text in texts if '%' not in text]
    associated_texts.append(filtered_texts)

# Function to clean and convert text to integer
def clean_and_convert(text):
    cleaned_text = re.sub(r'[^0-9]', '', text)  # Remove non-numeric characters
    return int(cleaned_text) if cleaned_text else None  # Convert to integer if possible

# Mapping of keywords to nutrition data fields
keyword_mapping = {
    "calories": "calories",
    "total fat": "totalFat",
    "saturated fat": "saturatedFat",
    "trans fat": "transFat",
    "cholesterol": "cholesterol",
    "sodium": "sodium",
    "carb": "totalCarbohydrate",
    "dietary fiber": "dietaryFiber",
    "sugars": "sugars",
    "protein": "protein",
    "vitamin a": "vitaminA",
    "vitamin c": "vitaminC",
    "calcium": "calcium",
    "iron": "iron",
    "vitamin d": "vitaminD",
    "potassium": "potassium",
    "serving size": "servingSize",
    "servings per container": "servingsPerContainer"
}

# Determine the number of columns based on the number of calorie values
calorie_columns = []
for text in associated_texts:
    if "calories" in text[0].lower():
        calorie_columns = [clean_and_convert(value) for value in text[1:] if clean_and_convert(value) is not None]
        break

# Create a list of nutrition data objects, one for each column
nutrition_data_list = [nutrition_data_template.copy() for _ in range(len(calorie_columns))]

# Populate the nutrition data objects with the extracted information
for text in associated_texts:
    parts = text
    for i in range(len(parts)):
        for keyword, field in keyword_mapping.items():
            if keyword in parts[i].lower():
                for col in range(len(calorie_columns)):
                    if i + col + 1 < len(parts):
                        value = clean_and_convert(parts[i + col + 1])
                        nutrition_data_list[col][field] = value
                break

# Print the structured data objects
for nutrition_data in nutrition_data_list:
    print(nutrition_data)