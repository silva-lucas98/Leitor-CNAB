from .models import Transaction


def handle_uploaded_file(request):
    uploaded_file = request.FILES["file"]

    for row in uploaded_file:
        string = row.decode()
        data = {
            "type": string[0],
            "date": string[1:9],
            "value": string[9:19],
            "cpf": string[19:30],
            "card": string[30:42],
            "hour": string[42:48],
            "owner": string[48:62].strip(),
            "store": string[62:80].strip(),
        }

        instance = Transaction.objects.create(**data)
        instance.save()
