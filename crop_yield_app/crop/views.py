from django.shortcuts import render
from .forms import CropInputForm
import google.generativeai as genai
from django.utils.safestring import mark_safe
import markdown
# Configure Gemini AI API
genai.configure(api_key="Here Insert Your Gemini AI API KEY")

def predict_crop_yield(request):
    response = None
    form = CropInputForm()  

    if request.method == 'POST':
        form = CropInputForm(request.POST)
        if form.is_valid():
            crop_data = form

            # Prompt for AI input
            prompt = f"""
            Provide a concise and actionable recommendation for better crop yield based on the following data:

            Crop: {crop_data['crop_name']}
            Soil Type: {crop_data['soil_type']}
            Include the following:

            1. Optimal NPK levels and soil pH for the specified crop and soil type.
            2. Fertilizer recommendations (both organic and inorganic) tailored to the crop and soil conditions.
            3. Companion plants that can be grown alongside the specified crop.
            4. Alternative crop suggestions if the specified crop is unsuitable for this soil type.

            The response should be detailed and structured into sections with headings.
            """

            # Fetch response from GenAI API
            model = genai.GenerativeModel("gemini-1.5-flash")
            api_response = model.generate_content(prompt)

            # Use the text response from GenAI API
            if api_response.text.strip():
                response = mark_safe(markdown.markdown(api_response.text))  
            else:
                response = "No recommendations available at the moment. Please try again."

    return render(request, 'crop/predict.html', {'form': form, 'response': response})
