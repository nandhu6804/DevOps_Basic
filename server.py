from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Function to determine BMI category
def calculate_bmi_category(bmi):
    if bmi <= 18.5:
        return "You're Underweight"
    elif 18.5 < bmi <= 24.9:
        return "You're Normal Weight"
    elif 24.9 < bmi <= 29.9:
        return "You're Overweight"
    else:
        return "You're Obese"

# Home route
@app.route('/')
def home():
    return "Welcome to the BMI Calculator! Please use the provided HTML form to calculate your BMI."

# BMI calculation route
@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi_route():
    data = request.json
    weight = data.get('weight')
    height = data.get('height')

    if weight is None or height is None:
        return jsonify({"error": "Invalid input"}), 400

    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    bmi_category = calculate_bmi_category(bmi)

    # Return result as JSON
    return jsonify({"bmi": round(bmi, 2), "category": bmi_category})

# Route to serve HTML files
@app.route('/<path:path>')
def send_html(path):
    return send_from_directory('', path)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
