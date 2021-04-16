from telegram import KeyboardButton,InlineKeyboardButton
class bottom:
    button_buyurtma = [
        [KeyboardButton(text="🛒 Buyurtma qilish")],
        [KeyboardButton(text="🛍 Buyurtmalarim"),
         KeyboardButton(text="👨‍👨‍👦 Evos oilasi")],
        [KeyboardButton(text="✍️Fikr bildirish"),
         KeyboardButton(text="⚙️sozlamalar")]
    ]

    button_lavash=[
        [InlineKeyboardButton("🌯 lavash go`shtli", callback_data="lavash_go`sht"),
         InlineKeyboardButton("🌯 Lavash tovuqli", callback_data="lavash_tovu")],
        [InlineKeyboardButton("⬅️Otrga", callback_data="ort")]
    ]
    button_dog = [
        [InlineKeyboardButton("🌭 Big Hot-Dog", callback_data="big"),
         InlineKeyboardButton("🌭 Mini Hot-Dog", callback_data="mini")],
        [InlineKeyboardButton("⬅️Otrga", callback_data="ort")]
    ]
    button_donar = [
        [InlineKeyboardButton("Donar Goshtli", callback_data="donargosht"),
         InlineKeyboardButton("Donar tovuqli ", callback_data="donartovuq")],
        [InlineKeyboardButton("⬅️Otrga", callback_data="ort")]
    ]
    button_set = [
        [InlineKeyboardButton("Combo1", callback_data="com1"),
         InlineKeyboardButton("Combo2", callback_data="com2")],
        [InlineKeyboardButton("Combo3", callback_data="com3"),
         InlineKeyboardButton("Combo4", callback_data="com4")],
        [InlineKeyboardButton("⬅️Otrga", callback_data="ort")]
    ]
    button_shaurma = [
        [InlineKeyboardButton("🥙 Shaurma goshtli", callback_data="goshli"),
         InlineKeyboardButton("🥙 Shaurma goshtli achhiq", callback_data="goshliachchiq")],
        [InlineKeyboardButton("🥙 Shaurma tovuqli", callback_data="tuvuqli"),
         InlineKeyboardButton("🥙 Shaurma tovuqli achhiq", callback_data="tovuqliachhiq")],
        [InlineKeyboardButton("⬅️Otrga", callback_data="ort")]
    ]
    button_burrger = [
        [InlineKeyboardButton("🍔 Gamburger", callback_data="gam"),
         InlineKeyboardButton("🍔 Chizburger ", callback_data="chiz")],
        [InlineKeyboardButton("⬅️Otrga", callback_data="ort")]
    ]
    button_des = [
        [InlineKeyboardButton("Asalim", callback_data="asalim"),
         InlineKeyboardButton("CHizkeyk", callback_data="chizkeyk")],
        [InlineKeyboardButton("Choco", callback_data="choco")],
        [InlineKeyboardButton("⬅️Otrga", callback_data="ort")]
    ]
    button_ichimlik = [
        [InlineKeyboardButton("💧suv", callback_data="suv"),
         InlineKeyboardButton("🍹 pepsi", callback_data="pepsi")],
        [InlineKeyboardButton("🍋 limon choy", callback_data="limonchoy"),
         InlineKeyboardButton("☕️ Kofe 3/1", callback_data="kofe 3/1")],
        [InlineKeyboardButton("☕ Qora coffe", callback_data="kofeqora")],
        [InlineKeyboardButton("⬅️Otrga", callback_data="ort")]
    ]
    button_gazak = [
        [InlineKeyboardButton("🍟 Free", callback_data="free"),
         InlineKeyboardButton("🥔 Qish.kartoshkasi", callback_data="qishkar")],
        [InlineKeyboardButton("🥗 Salat", callback_data="salt"),
         InlineKeyboardButton("🥫 Souslar", callback_data="sous")],
        [InlineKeyboardButton("🍚 Gruch", callback_data="guruch")],
        [InlineKeyboardButton("⬅️Otrga", callback_data="ort")]
    ]
    button_soni_set = [
        [InlineKeyboardButton("1️⃣", callback_data="bir"),
         InlineKeyboardButton("2️⃣", callback_data="ikki")],
        [InlineKeyboardButton("3️⃣", callback_data="uch"),
         InlineKeyboardButton("4️⃣", callback_data="tort")],
        [InlineKeyboardButton("5️⃣", callback_data="besh"),
         InlineKeyboardButton("6️⃣", callback_data="olti")],
        [InlineKeyboardButton("⬅️Otrga", callback_data="ortga_set")]
    ]
    button_soni_lashav = [
        [InlineKeyboardButton("1️⃣", callback_data="bir"),
         InlineKeyboardButton("2️⃣", callback_data="ikki")],
        [InlineKeyboardButton("3️⃣", callback_data="uch"),
         InlineKeyboardButton("4️⃣", callback_data="tort")],
        [InlineKeyboardButton("5️⃣", callback_data="besh"),
         InlineKeyboardButton("6️⃣", callback_data="olti")],
        [InlineKeyboardButton("⬅️Otrga", callback_data="ortga")]
    ]
    button_soni_shaurma = [
        [InlineKeyboardButton("1️⃣", callback_data="bir"),
         InlineKeyboardButton("2️⃣", callback_data="ikki")],
        [InlineKeyboardButton("3️⃣", callback_data="uch"),
         InlineKeyboardButton("4️⃣", callback_data="tort")],
        [InlineKeyboardButton("5️⃣", callback_data="besh"),
         InlineKeyboardButton("6️⃣", callback_data="olti")],
        [InlineKeyboardButton("⬅️Otrga", callback_data="ortga_shaurma")]
    ]
    button_soni_donar = [
        [InlineKeyboardButton("1️⃣", callback_data="bir"),
         InlineKeyboardButton("2️⃣", callback_data="ikki")],
        [InlineKeyboardButton("3️⃣", callback_data="uch"),
         InlineKeyboardButton("4️⃣", callback_data="tort")],
        [InlineKeyboardButton("5️⃣", callback_data="besh"),
         InlineKeyboardButton("6️⃣", callback_data="olti")],
        [InlineKeyboardButton("⬅️Otrga", callback_data="ortga_donar")]
    ]
    button_soni_bur = [
        [InlineKeyboardButton("1️⃣", callback_data="bir"),
         InlineKeyboardButton("2️⃣", callback_data="ikki")],
        [InlineKeyboardButton("3️⃣", callback_data="uch"),
         InlineKeyboardButton("4️⃣", callback_data="tort")],
        [InlineKeyboardButton("5️⃣", callback_data="besh"),
         InlineKeyboardButton("6️⃣", callback_data="olti")],
        [InlineKeyboardButton("⬅️Otrga", callback_data="ortga_bur")]
    ]
    button_soni_dog = [
        [InlineKeyboardButton("1️⃣", callback_data="bir"),
         InlineKeyboardButton("2️⃣", callback_data="ikki")],
        [InlineKeyboardButton("3️⃣", callback_data="uch"),
         InlineKeyboardButton("4️⃣", callback_data="tort")],
        [InlineKeyboardButton("5️⃣", callback_data="besh"),
         InlineKeyboardButton("6️⃣", callback_data="olti")],
        [InlineKeyboardButton("⬅️Otrga", callback_data="ortga_dog")]
    ]
    button_soni_des=[
        [InlineKeyboardButton("1️⃣", callback_data="bir"),
         InlineKeyboardButton("2️⃣", callback_data="ikki")],
        [InlineKeyboardButton("3️⃣", callback_data="uch"),
         InlineKeyboardButton("4️⃣", callback_data="tort")],
        [InlineKeyboardButton("5️⃣", callback_data="besh"),
         InlineKeyboardButton("6️⃣", callback_data="olti")],
        [InlineKeyboardButton("⬅️Otrga", callback_data="ortga_des")]
    ]
    button_soni_ich = [
        [InlineKeyboardButton("1️⃣", callback_data="bir"),
         InlineKeyboardButton("2️⃣", callback_data="ikki")],
        [InlineKeyboardButton("3️⃣", callback_data="uch"),
         InlineKeyboardButton("4️⃣", callback_data="tort")],
        [InlineKeyboardButton("5️⃣", callback_data="besh"),
         InlineKeyboardButton("6️⃣", callback_data="olti")],
        [InlineKeyboardButton("⬅️Otrga", callback_data="ortga_ich")]
    ]
    button_soni_gaz = [
        [InlineKeyboardButton("1️⃣", callback_data="bir"),
         InlineKeyboardButton("2️⃣", callback_data="ikki")],
        [InlineKeyboardButton("3️⃣", callback_data="uch"),
         InlineKeyboardButton("4️⃣", callback_data="tort")],
        [InlineKeyboardButton("5️⃣", callback_data="besh"),
         InlineKeyboardButton("6️⃣", callback_data="olti")],
        [InlineKeyboardButton("⬅️Otrga", callback_data="ortga_gaz")]
    ]
