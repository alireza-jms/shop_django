from shop.models import Product

class Cart:
    def __init__(self,request):
        self.session=request.session

        cart=self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key']={}

        self.cart = cart    
    
    def add(self, product,quantity):
        product_id=str(product.id)     #گرفتن درخواست اضافه به سبدخرید از ویو.کارت تابع ادکارت 
        product_qty=str(quantity)
        if product_id in self.cart:
            pass
        else:
           self.cart[product_id] =int(product_qty)
        self.session.modified=True

    def __len__(self):
     return len(self.cart)

    def get_prods(self):
       product_ids=self.cart.keys()
       products = Product.objects.filter(id__in=product_ids)  
       return products
    
    def get_quants(self):                    #تابع گرفتن تعداد  یک محصول و ارسال به سبد خرید در تمپلیت
       quantities=self.cart
       return quantities
    
    def get_total(self):     #جمع سفارشات داخل سبد خرید 
      #{"2":4}دو کیلد و 3 ولیو ما است
      products_ids=self.cart.keys()
      products=Product.objects.filter(id__in=products_ids)
      total=0
      for key,value in self.cart.items():
          key=int(key)
          for product in products:
           if product.id==key:
              total=total+(product.price *value)
      return total 

    def update(self, product, quantity):
       product_id=str(product)
       product_qty= int(quantity)

       ourcart=self.cart 
       ourcart[product_id]=product_qty
       self.session.modified =True
        
       alaki = self.cart
       return alaki

    def delete(self , product):
     product_id = str (product)
     if product_id in self.cart:
      del self.cart[product_id]

     self.session.modified =True


       