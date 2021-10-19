from django.shortcuts import render

# Create your views here.
def handle_uploaded_file(f, st):
    with open(str("static/" + st), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def textchecker(request):
    content = {
        "mylist1":"",
        "mylist2":"",
        "mis_match_percentage": 0,
        "calculated": 0,
    }
    if request.method == "POST":
        Text1 = request.POST['text1']
        Text2 = request.POST['text2']
        if 'file1' in request.FILES.keys():
            handle_uploaded_file(request.FILES['file1'], "file_txt1.txt")
            text_file = open("static/file_txt1.txt", "r")
            Text1 = text_file.read()
            text_file.close()
        if 'file2' in request.FILES.keys():
            handle_uploaded_file(request.FILES['file2'], "file_txt2.txt")
            text_file = open("static/file_txt2.txt", "r")
            Text2 = text_file.read()
            text_file.close()
        
        txt1list = Text1.splitlines()
        txt2list = Text2.splitlines()
        if (Text1 == "" or Text2 == ""):
            return render(request, "textchecker.html", content)
        mn_len = min(len(txt1list), len(txt2list))
        total_char = 0
        total_match = 0
        #added from here
        ind1 = []
        ind2 = []
        isdif1 = []
        isdif2 = []
        for id in range(len(txt1list)):
            ind1.append(id)
            isdif1.append(0)
            total_char += len(txt1list[id])
        for id in range(len(txt2list)):
            ind2.append(id)
            isdif2.append(0)
            total_char += len(txt2list[id])
        #added end here
        for row in range(mn_len):
            if txt1list[row] != txt2list[row]:
                isdif1[row] = 1
                isdif2[row] = 1 
            else:
                total_match += 2 * len(txt1list[row])
        if len(txt1list) != mn_len:
            for row in range(mn_len , len(txt1list)):
                isdif1[row] = 1
        elif len(txt2list) != mn_len:
            for row in range(mn_len , len(txt2list)):
                isdif2[row] = 1
        percentage = format((total_match / total_char) * 100, ".2f")
        mylist1 = zip(txt1list , ind1, isdif1)
        mylist2 = zip(txt2list , ind2, isdif2)
        content = {
            "mylist1": mylist1,
            "mylist2": mylist2,
            "mis_match_percentage": percentage,
            "calculated": 1,
        }
    return render(request, "textchecker.html", content)