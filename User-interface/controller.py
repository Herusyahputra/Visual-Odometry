from .User_Interface.Ui_Mainwindow import Ui_MainWindow
from moilutils import MoilUtils

class UiController(Ui_MainWindow):
    def __init__(self, mainWindow):
        super(UiController, self).__init__()
        self.parent = mainWindow
        self.setupUi(self.parent)
        self.connect_event()

    def connect_event(self):
        self.btn_open_image.clicked.connect(self.open_image)

    def open_image(self):
        """
        Function for open image. Open Dialog to search image file from Directory...

        Returns:
            showing to the window in user interface..
        """
        filename = MoilUtils.selectFile(self.parent, "Select Image", "../SourceImage",
                                            "Image Files (*.jpeg *.jpg *.png *.gif *.bmg)")
        if filename:
            self.image = MoilUtils.readImage(filename)
            self.h, self.w = self.image.shape[:2]
            # self.parent.setWindowTitle(self.title + " - " + filename)
            self.type_camera = MoilUtils.readCameraType(filename)
            MoilUtils.showImageToLabel(self.labe)
            if self.type_camera:
                self.onclick_normal()
                # self.label_camera.setText("Camera type: " + self.type_camera)
                self.show_percentage()

    def onclick_normal(self):
        """
        Change to normal view..

        Returns:

        """
        if self.image is not None:
            self.normal_view = True
            self.anypoint_view = False
            self.panorama_view = False
            self.scrollArea.show()
            self.show_to_window()
            self.reset_mode_view()