from imports import *

app = Flask(__name__, static_url_path="/storage/emulated/0", static_folder="/storage/emulated/0")


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")


@app.route("/photos", methods=["POST", "GET"])
def photos():
    all_files = []
    for photo in photos_dir:
        files_ = list_files(photo)
        for a_file in files_:
            all_files.append(a_file)
    photos = []
    for photo in all_files:
        if photo.rpartition('.')[-1] in photolst:
            photos.append(photo)
    return render_template(
        "photos.html", title="Photos", photos=photos, length=len(photos)
    )


@app.route("/documents")
def documents():
    all_files = []
    all_files_names = []
    for doc in document_dir:
        files_ = list_files(doc)
        files_names = list_files_name(doc)
        for a_file in files_:
            all_files.append(a_file)
        for a_file_name in files_names:
            all_files_names.append(a_file_name)
    documents = []
    documents_names = []
    for i in range(0,len(all_files)):
        if all_files[i].rpartition('.')[2] in doclst:
            documents.append(all_files[i])
            documents_names.append(all_files_names[i])
    return render_template(
        "document.html",
        title="Document",
        documents=documents,
        len=len(documents),
        document_name=documents_names,
    )


@app.route("/music")
def music():
    all_files = []
    all_files_names = []
    for music_ in music_dir:
        files_ = list_files(music_)
        files_names = list_files_name_shortened(music_)
        for a_file in files_:
            all_files.append(a_file)
        for a_file_name in files_names:
            all_files_names.append(a_file_name)
    ids = []
    music = []
    music_names = []
    for i in range(0,len(all_files)):
        if all_files[i].rpartition('.')[2] in musiclst:
            music.append(all_files[i])
            music_names.append(all_files_names[i])
    for i in range(1, len(music) + 1):
        ids.append(i)
    return render_template(
        "music.html",
        title="Music",
        music=music,
        len=len(music),
        music_name=music_names,
        ids=ids,
    )


@app.route("/video")
def video():
    all_files = []
    all_files_names = []
    for video_ in video_dir:
        files_ = list_files(video_)
        files_names = list_files_name(video_)
        for a_file in files_:
            all_files.append(a_file)
        for a_file_name in files_names:
            all_files_names.append(a_file_name)
    ids = []
    videos = []
    video_names = []
    for i in range(0,len(all_files)):
        if all_files[i].rpartition('.')[2] in videolst:
            videos.append(all_files[i])
            video_names.append(all_files_names[i])
        
    return render_template(
        "video.html",
        title="Video",
        videos=videos,
        len=len(videos),
        video_names=video_names,
    )


@app.route("/findPhone")
def findPhone():
    os.system('termux-media-player play iphone_6-30.ogg')
    return redirect('/home')


