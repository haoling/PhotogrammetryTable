Import("env")

platform = env.PioPlatform()

env.Prepend(
    UPLOADERFLAGS=[]
)
env.Append(
    UPLOADERFLAGS=[]
)
env.Replace(
    UPLOADER="$PROJECT_DIR/ftavrw/ftavrw.exe",
    UPLOADCMD="$UPLOADER $PLATFORMIO_UPLOAD_FLAGS $UPLOADERFLAGS $BUILD_DIR/firmware.hex"
)