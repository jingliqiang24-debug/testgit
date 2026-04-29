

shopping_cart = {}

info = """
###############
欢迎来到购物系统
1.添加商品
2.更新商品
3.删除商品
4.查询商品
5.退出系统
##############
"""
while True:
    print(info)
    choice = input("请选择")
    match choice:
        case "1":
            shop = input("请输入新增商品名称")
            price = float(input("请输入商品价格"))
            number = int(input("请输入商品数量"))
            if shop not in shopping_cart:
              shopping_cart[shop] = {"price":price,"number":number}
              print("新增成功")
            else:
                print("有该商品")
        case "2":
            shop = input("请输入更新商品名称")
            if shop  in shopping_cart:
                price = float(input("请输入商品价格"))
                number = int(input("请输入商品数量"))
                shopping_cart[shop] = {"price":price,"number":number}
            else:
                print("无该商品,请先添加")
        case "3":
            name = input("请输入删除商品的名称")
            if name not in shopping_cart:
                print("没有给商品,删除不了")
            else:
               del shopping_cart[name]
               print("删除成功")
        case "4":
            print("展示全部商品")
            for i in shopping_cart.keys():
                print(f"{i}:{shopping_cart[i]}")
        case "5":
            print("退出bye")
            break
        case _:
            print("非法操作,不支持")

