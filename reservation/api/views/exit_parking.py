from django.views.decorators.csrf import csrf_exempt
import json
from reservation.models import Reservation


@csrf_exempt
def exit_parking(request): 
    request_body = request.body.decode('utf-8')
    data = json.loads(request_body)
    parking_slot = data.get('parking_slot')
    current_user = request.user
    if not current_user.is_authenticated:
        return JsonResponse({"result": "you must login first"})
    try:
        reserved_parking_slot = Reservation.objects.filter(user_id=current_user.id, 
                                                           parking_slot=parking_slot).first()
        reserved_parking_slot.exit_date = timezone.now()
        reserved_parking_slot.save()
        return JsonResponse({"result": "your exit has been recorded!"})
    except Exception:
        return JsonResponse({"result": "the parking lot isn't reserved by you!"})