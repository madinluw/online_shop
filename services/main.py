from django.core.mail import send_mail


def order_data_sender_to_email(user, address, phone_number, message, products):
    send_mail(
            f'Заказ от {user}',
            f'На адрес {address}\nНомер телефона: {phone_number}\nCooбщение: {message}\nТовар: {", ".join(products)if len(products) > 1 else products[0]}',
            'from@example.com',
            ['muratbekovamadinaaa08@gmail.com'],
            fail_silently=False,
        )

