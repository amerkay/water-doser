from farmware_tools import device


class Logger:
    FARMWARE_NAME = "unknown farmware"
    LOGGER_LEVEL = 3

    @staticmethod
    def set_level(level):
        Logger.LOGGER_LEVEL = int(level) if int(level) in [0, 1, 2, 3] else 0
        device.log(
            "[{}] LOGGER_LEVEL set to {}".format(
                Logger.FARMWARE_NAME, Logger.LOGGER_LEVEL
            )
        )

    @staticmethod
    def log(message, message_type="debug", channels=[], title=""):
        """ Sends a log message

        Uses farmware_tools.device.log().

        Arguments:
            message {str} -- Message text

        Keyword Arguments:
            message_type {str} -- Message type (default: {'info'})
            channels {list} -- channels (default: {[]})
            title {str} -- extra title text to add to farmware name (default: {''})
        """
        if Logger.LOGGER_LEVEL == 0 and message_type != "error":
            return

        if title == "":
            log_message = "[{fwname}] {msg}".format(
                fwname=Logger.FARMWARE_NAME, msg=message
            )
        else:
            log_message = "[{fwname}: {title}] {msg}".format(
                fwname=Logger.FARMWARE_NAME, title=title, msg=message
            )

        device.log(message=log_message, message_type=message_type, channels=channels)
