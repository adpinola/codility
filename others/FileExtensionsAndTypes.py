typeMapping = {
    "mp3": "music",
    "aac": "music",
    "flac": "music",
    "jpg": "images",
    "bmp": "images",
    "gif": "images",
    "mp4": "movies",
    "avi": "movies",
    "mkv": "movies",
}

# Here I will store the accumulated size of each type
sizeMapping = {
    "music": 0,
    "images": 0,
    "movies": 0,
    "other": 0
}

def solution(S):
    # I'm not considering what happens if S is empty :)
    fileList = S.split('\n') # Let's get one record per file
    for record in fileList:
        fileFullName = record.split(' ')[0]
        fileExtension = fileFullName[::-1].split('.')[0][::-1]
        fileSize = int(record.split(' ')[1][:-1])
        if fileExtension in typeMapping:
            fileType = typeMapping[fileExtension]
            sizeMapping[fileType] += fileSize
        else:
            # Unknown Extension, so it defaults to 'other'
            sizeMapping["other"] += fileSize
    filesInfo = ''
    for key in sizeMapping:
        filesInfo += f'{key} {sizeMapping[key]}b\n'
    return filesInfo  