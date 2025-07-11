# Create your views here.
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request, 'mvapp/index.html')  # 首页上传界面

def generate_mv(request):
    if request.method == 'POST':
        photos = request.FILES.getlist('photos')
        inspiration = request.POST.get('inspiration')

        print("收到前端上传的照片数量：", len(photos))
        print("收到前端灵感内容：", inspiration)

        # 保存上传文件
        for photo in photos:
            fs = FileSystemStorage(location='media/uploads/')
            fs.save(photo.name, photo)

        # 你可以在这里处理“inspiration”内容（调用AI或生成MV）

        return redirect('mv_result')  # 跳转到结果页面
    return redirect('home')

def mv_result(request):
    return render(request, 'mvapp/create.html')  # MV结果页
