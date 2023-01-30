def handle_uploaded_file(request):
    uploaded_file = request.FILES["file"]

    for row in uploaded_file:
        string = row.decode()
        print(string)
