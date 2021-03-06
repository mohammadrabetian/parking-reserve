from reservation.models import Reservation
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import permission_required
from reservation.decorators.login_required import login_required
from reservation.decorators.request_method import check_request_method


@csrf_exempt
@login_required
@check_request_method(method="GET")
@permission_required("reservation.admin_role", login_url="forbiden_response/", raise_exception=False)
def active_reservations(request):
    reservations = Reservation.objects.filter(
        exit_date__isnull=True, enter_date__isnull=False
    ).values(
        "id",
        "created_date",
        "start_date",
        "finish_date",
        "parking_slot",
        "user__username",
    )
    if reservations:
        return JsonResponse({"result": list(reservations)}, status=200)
    return JsonResponse({"result": "There are no reservations right now!"}, status=404)
