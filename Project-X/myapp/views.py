from django.http import JsonResponse
from django.views.decorators.http import require_GET
from myapp.json_reader import read_json

@require_GET
def ping(request):
    return JsonResponse({'message': 'pong'})

def get_json_data_view(request):
    file_path = '/Users/marcosb/Documents/Schools/UCSC/SEQA.X401.-27--Object-Oriented-Program-And-Design/Project-X/backend/data.json'  # Absolute path to your JSON file
    data = read_json(file_path)
    if data is not None:
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"error": "Failed to load data"}, status=500)