from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import imaplib
import email


if __name__ == "__main__":
    class InteractionWithMail:
        GMAIL_SMTP = "smtp.gmail.com"
        GMAIL_IMAP = "imap.gmail.com"

        def __init__(self, login, password):
            self.login = login
            self.password = password
            self.recipients = ""
            self.heading = None

        def reassign_sender(self, new_log, new_pass):
            self.login = new_log
            self.password = new_pass

        def assign_recipients(self, *args):
            self.recipients = ', '.join([*args])

        def prepare_a_message(self, message, subject="Subject"):
            self.msg = MIMEMultipart()
            self.msg['From'] = self.login
            self.msg['To'] = self.recipients
            self.msg['Subject'] = subject
            self.msg.attach(MIMEText(message))

        def check_created_message(self, public=False):
            return f"""
Отправление из {self.login}{f" c паролем {self.password}" if public else ""}
Полное содержание:\n{self.msg.as_string()}
"""

        def send_a_message(self, port=587):
            try:
                if self.recipients == "":
                    raise ValueError("Вы не задали получателей через 'assign_recipients'")
                elif self.msg.as_string():
                    pass
            except AttributeError:
                raise ValueError("Вы ещё не создали сообщение через 'prepare_a_message'")

            try:
                self.ms = smtplib.SMTP(self.GMAIL_SMTP, port)

                self.ms.ehlo()
                self.ms.starttls()
                self.ms.ehlo()

                self.ms.login(self.login, self.password)

                self.ms.sendmail(
                    self.login,
                    self.recipients,
                    self.msg.as_string()
                )
                self.ms.quit()

                return True

            except Exception as e:
                raise AssertionError(f"Произошла ошибка {e.__class__.__name__}")

        def choose_a_title(self, heading):
            self.heading = heading

        def receive_emails(self):
            self.mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
            self.mail.login(self.login, self.password)
            self.mail.list()
            self.mail.select("INBOX")

            self.status, self.data = self.mail.uid(
                'search',
                None,
                f"(HEADER Subject {self.heading})" if self.heading else 'ALL'
            )

            if self.data[0]:
                pass
            else:
                raise AssertionError('Нужная информация в письме отсутствует')

            try:
                self.latest_email_uid = self.data[0].split()[-1]

                self.status, self.data = self.mail.uid(
                    'fetch',
                    None,
                    self.latest_email_uid, '(RFC822)'
                )

                self.raw_email = self.data[0][1]

                self.email_message = email.message_from_bytes(self.raw_email)

                self.mail.logout()

                return self.email_message

            except Exception as e:
                raise AssertionError(f"Произошла ошибка {e.__class__.__name__}")


# Демонстрация работоспособности, но только почты не рабочие
obj_word = InteractionWithMail('login@gmail.com', 'qwerty')
obj_word.prepare_a_message("Что нибудь интересное", subject="А тебе письмо!")
obj_word.assign_recipients('vasya@email.com', 'petya@email.com')

# Созданное сообщение
print(obj_word.check_created_message())
# Отправка и сохранение
email_content = obj_word.send_a_message()



# А я думал что классов MIMEText и MIMEMultipart совсем нет и их нужно реализовать,
# потому что модуля отдельно для каждого из них больше находилось
# Ну и сделал, а они теперь вон где оказываются теперь
#
# class MIMEText:
#     def __init__(self, message):
#         self.__content = message
#
#     def __repr__(self):
#         return self.__content
#
#
# class MIMEMultipart:
#     def __init__(self):
#         self.__string = """"""
#
#     def __setitem__(self, key, value):
#         self.__string += f"{key}: {value}\n"
#
#     def attach(self, message):
#         self.__string += f"\n{message}"
#
#     def full_string(self):
#         return self.__string