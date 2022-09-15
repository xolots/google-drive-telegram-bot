class config:
    BOT_TOKEN = "5646012306:AAHAroYClOBFWjbfQYA5ov2AEVMspEI8gEY"
    APP_ID = "18198572"
    API_HASH = "e6a21a5cfbc9cef50d22189ca2b92d02"
    DATABASE_URL = "postgres://umknvycwrcwkez:fc0c956777d163e7da42ec492ea2323b45c7f8dc14dd84e318e6f9c1d8e3c38c@ec2-3-229-165-146.compute-1.amazonaws.com:5432/d3q4h1mh5hnn9h"
    SUDO_USERS = "582570180" # Sepearted by space.
    SUPPORT_CHAT_LINK = "https://t.me/+FEXivaz5Yx82ZjY9"
    DOWNLOAD_DIRECTORY = "./downloads/"
    G_DRIVE_CLIENT_ID = "239316202399-f4o1jmdnv71gtuon9opdnmi3ts9lkfel.apps.googleusercontent.com"
    G_DRIVE_CLIENT_SECRET = "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"


class BotCommands:
  Download = ['download', 'dl']
  Authorize = ['auth', 'authorize']
  SetFolder = ['setfolder', 'setfl']
  Revoke = ['revoke']
  Clone = ['copy', 'clone']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash']
  YtDl = ['ytdl']

class Messages:
    START_MSG = "**Halo {}.**\n__Aku adalah Google Drive Uploader Bot.Kamu bisa mengupload file,photo / video ke Google Drive melalui directlink ataupun dari telegram.__\n__Kamu bisa membaca tutorial disini /help.__"

    HELP_MSG = [
        ".",
        "**Google Drive Uploader**\n__Aku bisa mengupload file dari direct link ataupun telegram ke google drive kamu. Yang perlu aku lakukan adalah mengautentikasi kamu dan kamu dapat mengirim link download langsung ataupun file,photo,gambar,dokumen melalui Telegram.__\n\nAku punya banyak fitur... ! Pengen Tau ? Baca Tutorial Berikut Dengan Hati-Hati.",
        
        f"**Autentikasi Google Drive**\n__Kirim /{BotCommands.Authorize[0]} commmand dan kamu akan mendapatkan URL, klik URL dan ikuti petunjuk yang ada dan tempel kode yang kamu dapat disini. Gunakan /{BotCommands.Revoke[0]} untuk logout dari akun google kamu.__\n\n**Catatan: Aku tidak akan mendengarkan perintah/command apapun (kecuali /{BotCommands.Authorize[0]} command) sampai kamu mengauterisasi aku.\nJadi, Autorisasi itu wajib !**",
        
        f"**Direct Links**\n__Kirim aku directlink yang dapat di download dan aku akan menyimpannya di server dan mengupload nya di google drive kamu. Kamu bisa menamai file sebelum di upload di google drive. Kirim aku url dan nama file dipisahkan dengan ' | '.__\n\n**__Contoh:__**\n```https://example.com/AFileWithDirectDownloadLink.mkv | New FileName.mkv```\n\n**Telegram Files**\n__Untuk mengupload file telegram ke google drive kamu, kamu hanya perlu mengirim ke sini dan aku akan menguploadnya ke google drive. Catatan: Mendownload File telegram lambat. jadi membutuhkan banyak waktu jika ukuran file besar.__\n\n**YouTube-DL Support**\n__Download files melalui youtube-dl.\nGunakan /{BotCommands.YtDl[0]} (YouTube Link/YouTube-DL Supported site link [DEV])__",
        
        f"**Custom Folder for Upload**\n__ingin mengupload di folder pilihan kamu?__ **TeamDrive** __ ?\nGunakan /{BotCommands.SetFolder[0]} (Folder URL) untuk mengubah folder upload.\nSemua file akan di upload di folder yang kamu pilih.__",
        
        f"**Hapus Google Drive Files**\n__Hapus file Google Drive. Gunakan /{BotCommands.Delete[0]} (File/Folder URL) untuk menghapus file atau balas /{BotCommands.Delete[0]} pesan ke bot.\nKamu bisa membersihkan Sampah/Trash /{BotCommands.EmptyTrash[0]}\nCatatan: File dihapus secara permanen. Proses ini tidak bisa dibatalkan.\n\n**Copy Google Drive Files**\n__Yuppp!!, Clone atau Copy Google Drive Files.\n__Gunakan /{BotCommands.Clone[0]} (File id / Folder id atau URL) untuk copy file di akun google drive kamu.__",
        
        "**Peraturan dan Ketentuan**\n__1. Jangan copy file berukuran besar. Hal ini dapat menyebabkan bot menjadi hang.\n2. Kirim hanya 1 request kecuali bot sudah menyelesaikan semua proses.\n3. Jangan mengirim link lambat @transload dulu.\n4. Jangan membuat overload atau menyalahgunakan layanan ini.__",
        
        # Dont remove this ↓ if you respect developer.
        "**Developed by @viperadnan and @xolots404**"
        ]
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **Rate Limit Exceeded.**\n__User rate limit exceeded try after 24 hours.__"
    
    FILE_NOT_FOUND_MESSAGE = "❗ **File/Folder tidak ditemukan.**\n__File id - {} tidak ditemukan. Pastikan file ada dan bisa diakses.__"
    
    INVALID_GDRIVE_URL = "❗ **Invalid Google Drive URL**\nPastikan link Google Drive sesuai dengan format."
    
    COPIED_SUCCESSFULLY = "✅ **Berhasil Di COpy.**\n[{}]({}) __({})__"
    
    NOT_AUTH = f"🔑 **Kamu tidak terautentikasi di akun manapun.**\n__Kirim /{BotCommands.Authorize[0]} untuk mengautentikasi.__"
    
    DOWNLOADED_SUCCESSFULLY = "📤 **Mengupload File...**\n**Namafile:** ```{}```\n**Ukuran:** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **Berhasil Di Upload.**\n[{}]({}) __({})__"
    
    DOWNLOAD_ERROR = "❗**Gagal Mendownload**\n{}\n__Link - {}__"
    
    DOWNLOADING = "📥 **Mendownload File...\nLink:** ```{}```"
    
    ALREADY_AUTH = "🔒 **Akun sudah terauntetikasi.**\n__Gunakan /revoke untuk logout.__\n__Kirimkan directlink ataupun file yang akan di upload ke Google Drive__"
    
    FLOW_IS_NONE = f"❗ **Invalid Code**\n__Jalankan {BotCommands.Authorize[0]} dulu.__"
    
    AUTH_SUCCESSFULLY = '🔐 **Akun Berhasil Di Autorisasi.**'
    
    INVALID_AUTH_CODE = '❗ **Invalid Code**\n__Code yang kamu kirim invalid atau sudah digunakan sebelumnya. Generate kode baru dengan link autorisasi URL__'
    
    AUTH_TEXT = "⛓️ **Untuk autorisasi akun kamu kunjungi url berikut [URL]({}) dan kirim kode yang kamu dapat ke sini.**\n__kunjungi URL > Allow permissions > kamu akan mendapatkan kode > copy > Kirim ke sini__"
    
    DOWNLOAD_TG_FILE = "📥 **Mendownload File...**\n**Nama File:** ```{}```\n**Ukuran:** ```{}```\n**MimeType:** ```{}```"
    
    PARENT_SET_SUCCESS = '🆔✅ **Custom Folder berhasil di ubah.**\n__custom folder id kamu - {}\nGunakan__ ```/{} clear``` __untuk menghapus.__'
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **Custom Folder ID Berhasil Di Bersihkan.**\n__Use__ ```/{BotCommands.SetFolder[0]} (Folder Link)``` __untuk menambahkannya kembali__.'
    
    CURRENT_PARENT = "🆔 **Custom Folder ID kamu - {}**\n__Gunakan__ ```/{} (Folder link)``` __untuk mengubahnya.__"
    
    REVOKED = f"🔓 **Berhasil logout.**\n__Gunakan /{BotCommands.Authorize[0]} untuk autorisasi dan menggunakan bot ini.__"
    
    NOT_FOLDER_LINK = "❗ **Invalid folder link.**\n__Link yang kamu berikan bukan folder.__"
    
    CLONING = "🗂️ **Cloning ke Google Drive...**\n__G-Drive Link - {}__"
    
    PROVIDE_GDRIVE_URL = "**❗ Provide a valid Google Drive URL along with commmand.**\n__Gunakan - /{} (GDrive Link)__"
    
    INSUFFICIENT_PERMISSONS = "❗ **Kamu tidak mempunyai akses ke file ini.**\n__File id - {}__"
    
    DELETED_SUCCESSFULLY = "🗑️✅ **File berhasil di hapus.**\n__File Dihapus Permanen !\nFile id - {}__"
    
    WENT_WRONG = "⁉️ **ERROR: SOMETHING WENT WRONG**\n__Please try again later.__"
    
    EMPTY_TRASH = "🗑️🚮**Berhasil membersihkan Trash/Sampah !**"
    
    PROVIDE_YTDL_LINK = "❗**Provide a valid YouTube-DL supported link.**"
