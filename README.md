# number2words

![Build Status](https://img.shields.io/github/actions/workflow/status/yourusername/number2words/ci.yml?branch=main)
![Coverage](https://img.shields.io/codecov/c/github/yourusername/number2words)
![License](https://img.shields.io/github/license/yourusername/number2words)

**number2words** یک کتابخانه‌ی پایتون برای تبدیل خودکار اعداد به حروف در زبان‌های فارسی و انگلیسی است.

## ویژگی‌ها

* پشتیبانی از اعداد صحیح مثبت و منفی
* پشتیبانی از زبان‌های انگلیسی (`en`) و فارسی (`fa`)
* رابط کاربری آسان برای توسعه‌دهندگان
* قابل استفاده به‌صورت ماژول، CLI و در پروژه‌های بزرگ‌تر

## نصب

```bash
pip install git+https://github.com/rezatutor475/number2words.git
```

## استفاده ساده

```python
from number2words import convert_number

print(convert_number(123, lang="en"))  # one hundred twenty three
print(convert_number(456, lang="fa"))  # چهارصد و پنجاه و شش
```

## استفاده در خط فرمان

```bash
number2words 890 --lang fa
```

### خروجی:

```
هشتصد و نود
```

## تست‌ها

```bash
pytest
```

## ساختار پروژه

```
number2words/
├── __init__.py
├── converter.py
├── en.py
├── fa.py
├── exceptions.py
├── cli.py
└── tests/
    ├── __init__.py
    ├── test_en.py
    └── test_fa.py
```

## درخواست مشارکت

ما از مشارکت شما استقبال می‌کنیم!

### چگونه مشارکت کنید:

1. این مخزن را Fork کنید.
2. یک شاخه جدید ایجاد کنید: `git checkout -b feature/new-feature`
3. تغییرات خود را اعمال کرده و Commit کنید: `git commit -m 'افزودن قابلیت جدید'`
4. به مخزن اصلی Pull Request بفرستید.

### قوانین مشارکت:

* قبل از هر commit، تست‌ها را اجرا کنید.
* از PEP8 پیروی کنید.
* توضیحات کافی برای Pull Request بنویسید.

## مجوز

این پروژه تحت مجوز MIT ارائه شده است. برای اطلاعات بیشتر به فایل LICENSE مراجعه کنید.
