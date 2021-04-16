from telegram import Update, KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, \
    CallbackQuery
from telegram.ext import CommandHandler, MessageHandler, Updater, ConversationHandler, CallbackContext, Filters, \
    InlineQueryHandler, CallbackQueryHandler
import urllib

from lavash_bottom import bottom

b = bottom()

from bot_2 import baza

bb = baza()
# bb.call(1)

button_line = [
    [InlineKeyboardButton("📖 Barcha menyular", url="https://telegra.ph/TASHKENT-EVOS-MENU-02-03"),
     InlineKeyboardButton('🍟🌯🥤 Set', callback_data="set")],
    [InlineKeyboardButton('🌯 lavash', callback_data='lavash'),
     InlineKeyboardButton('🌮 Shaurma', callback_data="shaur")],
    [InlineKeyboardButton('🍲 Donar', callback_data="donar"),
     InlineKeyboardButton('🍔 Burger', callback_data="bur")],
    [InlineKeyboardButton('🌭 Hot-Dog', callback_data="dog"),
     InlineKeyboardButton('🍰 Desertlar', callback_data="des")],
    [InlineKeyboardButton('☕ Ichimliklar', callback_data="ichimlik"),
     InlineKeyboardButton('🍟 Gazaklar', callback_data="gaz")]
]


def start(update, context):
    usee = update.message.from_user
    update.message.reply_text("Quyidagilardan birini tanlang",
                              reply_markup=ReplyKeyboardMarkup(b.button_buyurtma, resize_keyboard=True))
    return 1


def food_list(update, context):
    msg = update.message.text
    if msg == "🛒 Buyurtma qilish":
        update.message.reply_text("Bizning ovqatlarimiz ro'yxati 😋😋😋😋😋 ",
                                  reply_markup=InlineKeyboardMarkup(button_line))
    if msg == "✍️Fikr bildirish":
        update.message.reply_text("@Sayfidinov ga yozing")
    if msg == "🛍 Buyurtmalarim":
        update.message.reply_text("Siz hali hanuz birorta ham buyurtma bermagansiz.")
    if msg == "👨‍👨‍👦 Evos oilasi":
        update.message.reply_text("Botning xatolari ustida ishlari olib borilmoqda tez kunda xabarberamiz")
    if msg == "⚙️sozlamalar":
        update.message.reply_text("Botning xatolari ustida ishlari olib borilmoqda tez kunda xabarberamiz")


def choose_food(update, context):
    query = update.callback_query
    query.answer()
    """alll"""
    if query.data == "ort":
        update.callback_query.edit_message_text("Bizning ovqatlarimiz ro'yxati 😋😋😋😋😋 ",
                                                reply_markup=InlineKeyboardMarkup(button_line))
    """set"""
    if query.data == "set":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_set))
    if query.data == "com1":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_soni_set))
    if query.data == "com2":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_soni_set))
    if query.data == "com3":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_soni_set))
    if query.data == "com4":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_soni_set))
    if query.data == "ortga_set":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_set))
    """lavash"""
    if query.data == "lavash":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_lavash))
    if query.data == "lavash_go`sht":
        update.callback_query.edit_message_text("sonini tanlang ",
                                                reply_markup=InlineKeyboardMarkup(b.button_soni_lashav))
    if query.data == "besh":
        update.callback_query.edit_message_text(f"{bb.call(1) * 5} wertyl")
    if query.data == "lavash_tovu":
        update.callback_query.edit_message_text("sonini tanlang ",
                                                reply_markup=InlineKeyboardMarkup(b.button_soni_lashav))
    if query.data == "ortga":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_lavash))
    """shaurma"""
    if query.data == "shaur":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_shaurma))
    if query.data == "goshli":
        update.callback_query.edit_message_text("Turini tanlang ",
                                                reply_markup=InlineKeyboardMarkup(b.button_soni_shaurma))
    if query.data == "goshliachchiq":
        update.callback_query.edit_message_text("Turini tanlang ",
                                                reply_markup=InlineKeyboardMarkup(b.button_soni_shaurma))
    if query.data == "tuvuqli":
        update.callback_query.edit_message_text("Turini tanlang ",
                                                reply_markup=InlineKeyboardMarkup(b.button_soni_shaurma))
    if query.data == "tovuqliachhiq":
        update.callback_query.edit_message_text("Turini tanlang ",
                                                reply_markup=InlineKeyboardMarkup(b.button_soni_shaurma))
    if query.data == "ortga_shaurma":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_shaurma))
    """donar"""
    if query.data == "donar":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_donar))
    if query.data == "donargosht":
        update.callback_query.edit_message_text("Turini tanlang ",
                                                reply_markup=InlineKeyboardMarkup(b.button_soni_donar))
    if query.data == "donartovuq":
        update.callback_query.edit_message_text("Turini tanlang ",
                                                reply_markup=InlineKeyboardMarkup(b.button_soni_donar))
    if query.data == "ortga_donar":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_donar))
    """burger"""
    if query.data == "bur":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_burrger))
    if query.data == "gam":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_soni_bur))
    if query.data == "chiz":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_soni_bur))
    if query.data == "ortga_bur":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_burrger))
    """xot-dog"""
    if query.data == "dog":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_dog))
    if query.data == "big":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_soni_dog))
    if query.data == "mini":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_soni_dog))
    if query.data == "ortga_dog":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_dog))
    """desert"""
    if query.data == "des":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_des))
    if query.data == "asalim":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_soni_des))
    if query.data == "chizkeyk":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_soni_des))
    if query.data == "choco":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_soni_des))
    if query.data == "ortga_des":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_des))
    """ichimlik"""
    if query.data == "ichimlik":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_ichimlik))
    if query.data == "suv":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_soni_ich))
    if query.data == "pepsi":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_soni_ich))
    if query.data == "limonchoy":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_soni_ich))
    if query.data == "kofe 3/1":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_soni_ich))
    if query.data == "kofeqora":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_soni_ich))
    if query.data == "ortga_ich":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_ichimlik))
    """gaz"""
    if query.data == "gaz":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_gazak))
    if query.data == "free":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_soni_gaz))
    if query.data == "qishkar":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_soni_gaz))
    if query.data == "salt":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_soni_gaz))
    if query.data == "sous":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_soni_gaz))
    if query.data == "guruch":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_soni_gaz))
    if query.data == "ortga_gaz":
        update.callback_query.edit_message_text("Turini tanlang ", reply_markup=InlineKeyboardMarkup(b.button_gazak))
    if query.data == "bir_l":
        update.callback_query.edit_message_text([15000 * 1])
    if query.data == "ikki_l":
        update.callback_query.edit_message_text([15000 * 2])
    if query.data == "uch_l":
        update.callback_query.edit_message_text([15000 * 3])
    if query.data == "tort_l":
        update.callback_query.edit_message_text([15000 * 4])
    if query.data == "besh_l":
        update.callback_query.edit_message_text([15000 * 5])
    return 2


def main():
    ubd = Updater("1447543344:AAEh5Fn-RDcMXaK_4l29aOkDFm7nNCaOWeY", use_context=True)
    dsp = ubd.dispatcher
    dsp.add_handler(CallbackQueryHandler(choose_food))
    conver_hand = ConversationHandler(
        entry_points=[
            CommandHandler("start", start)
        ],
        states={
            1: [MessageHandler(Filters.text, food_list)],
            2: [MessageHandler(Filters.text, food_list)]
            # 3: [CallbackQueryHandler(back)],
            # 4: [CallbackQueryHandler(choose_food2)],
            # 5: [CallbackQueryHandler(back2)]
        },
        fallbacks=[CommandHandler("start", start)]
    )
    # dsp.add_handler(("start",start))
    dsp.add_handler(conver_hand)
    ubd.start_polling()
    ubd.idle()


if __name__ == '__main__':
    main()
