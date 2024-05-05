from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
import random ,os
from tkinter import messagebox
import tempfile

class Bill_App:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x800+0+0')
        self.root.title('Billing software') 

    # =======================Varibles=========================
        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.bill_no = StringVar()
        z= random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email = StringVar()
        self.c_search_bill = StringVar()
        self.c_product = StringVar()
        self.c_price = IntVar()
        self.c_qty = IntVar()
        self.c_subtotal = StringVar()
        self.c_taxtotal = StringVar()
        self.c_total = StringVar()


    #product Categories list
        self.category=["Select Options" , "Clothing" , "Lifestyles", "Mobiles"]
        self.SubcatClothing = ["Pant" , "T-shirt" , "Shirt"]
        
        self.Pant = ["Levis" , "Mufti" , "Spyker"]
        self.Price_Levies = 5000
        self.Price_Mufti = 3000
        self.Price_Spyker = 8000

        self.Tshirt = ["polo" , "lascoot" , "gant"]
        self.Price_polo = 1500
        self.Price_lascoot = 1000
        self.Price_gant = 900

        self.Shirt = ["Peter England" , "Louis Phillipe" , "Park Avenue"]
        self.Price_peterend = 2100
        self.Price_louisp = 1500
        self.Price_parkav = 2000

        self.SubcatLifestyle = ["Bath Soup" , "Face Cream" , "Hair Oil"]

        self.Bathsoup = ["Lifeboy" , "Santoor" , "Pearls"]
        self.price_lifeboy = 20
        self.price_santoor = 25
        self.price_peals = 20

        self.FaceCream = ["Ponds" , "Fair&lovely" , "Olay"]
        self.price_Ponds = 200
        self.price_Fairlovely = 250
        self.price_Olay = 350

        self.Hairoil = ["Parachute" , "jasmin" , "Bajaj"]
        self.price_Parachute = 150
        self.price_jasmin = 130
        self.price_Bajaj = 200
        
        self.SubcatMobiles = ["Iphone" , "Samsung" , "oneplus" ]

        self.Iphone = ["Iphone 11" , "Iphone 12" , "Iphone 13" ]
        self.price_Iphone11= 90000
        self.price_Iphone12= 120000
        self.price_Iphone13= 150000

        self.Sumsang = ["Galaxy01 " , "S1 Ultra" , "S1 pro3" ]
        self.price_Galaxy01 = 50000
        self.price_S1_Ultra= 120000
        self.price_S1_pro= 150000

        self.Oneplus = ["oneplusT" , "oneplusTpro" , "oneplus8T" ]
        self.price_oneplusT= 90000
        self.price_oneplusTpro= 20000
        self.price_oneplus8T= 45000



    #image 1
        img = Image.open("D:/tkinter/images/one.jpg")
        #taking image from a location
        img = img.resize((510,130),Image.Resampling.LANCZOS)
        #then resize it as per need ANTIALIAS (Resampling.LANCZOS)is for reducing quality of image
        self.photoimg = ImageTk.PhotoImage(img)
        # using that image in tkinter by using ImageTk.PhotoImage(varible)

        lbl_img =Label(self.root , image=self.photoimg)
        #displaying imageusing Label
        lbl_img.place(x=0,y=0,width=510 , height =130)
        #if height and width are not same as it was taken at the time of image resize 
        #while place it will not full image

    #image2
        img2 = Image.open("D:/tkinter/images/desktop_wallpaper__10-559.jpg")
        img2 = img2.resize((510,130),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbl_img2 =Label(self.root , image=self.photoimg2)
        lbl_img2.place(x=510,y=0,width=510 , height =130)

    #image3
        img3 = Image.open("D:/tkinter/images/youtube.png")
        img3 = img3.resize((510,130),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbl_img3 =Label(self.root , image=self.photoimg3)
        lbl_img3.place(x=1020,y=0,width=510 , height =130)


       # creating main label title
        lbl_title = Label(self.root , text="BILLING  SOFTWARE" , font=("Times new roman", 35,"bold"),bg="white", fg="blue")
        lbl_title.place(x=0 ,y=130 , width=1530 , height=45)


    #creating  Main Frames to place items in it

        main_frame = Frame(self.root,bd=5,relief=GROOVE,background="white")
        main_frame.place(x=0, y=175 , width=1530 , height=620)

        # creating customer label frame

        customer_frame = LabelFrame(main_frame , text="Customer" , font=("Times new roman", 12,"bold") , bg="white" , fg="red")
        customer_frame.place(x=10 , y=5 , width=350,height=140)

        #crating fields for customer frame

        lbl_mob = Label(customer_frame,text="Mobile No.", font=("arial", 12,"bold") , bg="white" ,bd=4 )
        lbl_mob.grid(row=0 , column=0 , stick = W , padx=5 ,pady=2)

        entry_mob = ttk.Entry(customer_frame, textvariable=self.c_phon,  font=("arial", 12,"bold") , width=19)
        entry_mob.grid(row=0,column=1 , stick = W , padx=5 ,pady=2)


        lbl_custname = Label(customer_frame,text="Customer Name ", font=("arial", 12,"bold") , bg="white" , bd=4)
        lbl_custname.grid(row=2 , column=0 , stick = W , padx=5 ,pady=2)

        entry_custname = ttk.Entry(customer_frame, textvariable=self.c_name, font=("arial", 10,"bold") ,  width=24)
        entry_custname.grid(row=2,column=1 ,stick = W , padx=5 ,pady=2)


        lbl_email = Label(customer_frame,text=" Email ", font=("arial", 12,"bold") , bg="white" ,bd=4)
        lbl_email.grid(row=3 , column=0 , stick = W , padx=5 ,pady=2)

        entry_email = ttk.Entry(customer_frame,  textvariable=self.c_email,  font=("arial", 10,"bold") , width=24)
        entry_email.grid(row=3,column=1 , stick = W , padx=5 ,pady=2)

   # creating product label frame

        product_frame = LabelFrame(main_frame , text="Product" , font=("Times new roman", 12,"bold") , bg="white" , fg="red")
        product_frame.place(x=370 , y=5 , width=650,height=140)


        #creting label and entry boxes 
        #category
        
        lbl_category = Label(product_frame,text="Select Categories", font=("arial", 12,"bold") , bg="white" ,bd=4)
        lbl_category.grid(row=0  , column=0 , stick = W , padx=5 ,pady=2)

        self.Combo_Category = ttk.Combobox(product_frame ,values= self.category ,font=("arial", 10,"bold"), width=24 , state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0  , column=1 , stick = W , padx=5 ,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>", self.Categories)

        #subcategory
        lbl_subcategory = Label(product_frame,text="Sub Categories", font=("arial", 12,"bold") , bg="white" ,bd=4)
        lbl_subcategory.grid(row=1  , column=0 , stick = W , padx=5 ,pady=2)

        self.Combo_subcategory = ttk.Combobox(product_frame , value=[""],font=("arial", 10,"bold"), width=24 , state="readonly")
        self.Combo_subcategory.grid(row=1  , column=1 , stick = W , padx=5 ,pady=2)
        self.Combo_subcategory.bind("<<ComboboxSelected>>", self.Product_add)
        

        #Product Name
        lbl_product = Label(product_frame,text="Select Product", font=("arial", 12,"bold") , bg="white" ,bd=4)
        lbl_product.grid(row=2  , column=0 , stick = W , padx=5 ,pady=2)

        self.combo_product = ttk.Combobox(product_frame ,textvariable=self.c_product ,font=("arial", 10,"bold"), width=24 , state="readonly")
        self.combo_product.grid(row=2  , column=1 , stick = W , padx=5 ,pady=2)
        self.combo_product.bind("<<ComboboxSelected>>", self.productprice)

        
        #price
        lbl_price = Label(product_frame,text="Price", font=("arial", 12,"bold") , bg="white" ,bd=4)
        lbl_price.grid(row=0  , column=2 , stick = W , padx=5 ,pady=2)

        self.combo_price = ttk.Combobox(product_frame ,textvariable=self.c_price ,font=("arial", 10,"bold"), width=24 , state="readonly")
        self.combo_price.grid(row=0  , column=3 , stick = W , padx=5 ,pady=2)

        #Qty
        lbl_qty =Label(product_frame,text="Quantity", font=("arial", 12,"bold") , bg="white" ,bd=4)
        lbl_qty.grid(row=1  , column=2 , stick = W , padx=5 ,pady=2)
      
        combo_qty = ttk.Entry(product_frame ,textvariable=self.c_qty ,font=("arial", 10,"bold"), width=26)
        combo_qty.grid(row=1 , column=3,stick = W , padx=5 ,pady=2)

    #Middle frame

        MiddleFrame = Frame(main_frame , bd=10)
        MiddleFrame.place(x=10 ,y=150, width=982, height=340)

    #image4
        img4 = Image.open("D:/tkinter/images/7898489.jpg")
        img4 = img4.resize((490,340),Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lbl_img4 =Label(MiddleFrame , image=self.photoimg4)
        lbl_img4.place(x=0,y=0,width=490 , height =340)

    #image5
        img5 = Image.open("D:/tkinter/images/3699487.jpg")
        img5 = img5.resize((490,340),Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lbl_img5 =Label(MiddleFrame , image=self.photoimg5)
        lbl_img5.place(x=490,y=0,width=510 , height =340)






    # Search bill Area
        Search_frame = Frame(main_frame , bd=2 , bg="white")
        Search_frame.place(x=1035,y=15 , width=480, height=40)

        #creating label for bill search
        lbl_Bill_no =Label(Search_frame,text="Bill number", font=("arial", 12,"bold") , bg="red" ,fg="white")
        lbl_Bill_no.grid(row=0  , column=0 , stick = W , padx=1 ,pady=1)

        Bill_no_entry = ttk.Entry(Search_frame , textvariable=self.c_search_bill,font=("arial", 10,"bold"), width=26)
        Bill_no_entry.grid(row=0 , column=1,stick = W , padx=2 )
        
        btnBillSearch =Button(Search_frame, command=self.find_bill, text="Search" ,font=("arial", 10,"bold"),bg="orangered" ,fg="white",width=15, cursor="hand2")
        btnBillSearch.grid(row=0,column=2)







    #right Frame  Bill area 
        RightLabelFrame = LabelFrame(main_frame,text="Bill Area" , font=("Times new roman", 12,"bold") , bg="white" , fg="red")
        RightLabelFrame.place(x=1035,y=45, width=480 , height=440)

        scroll_y = Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea =Text(RightLabelFrame, yscrollcommand=scroll_y.set , bg="white" ,fg="blue"  , font=("Times new roman", 12,"bold"))
        scroll_y.pack(side = RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)



    # creating Bill Counter label frame

        bottom_frame = LabelFrame(main_frame , text="Bill Counter" , font=("Times new roman", 12,"bold") , bg="white" , fg="red")
        bottom_frame.place(x=0 , y=485 , width=1530,height=125)

        #creating entry fields for bill counter
        lbl_subtotal =Label(bottom_frame,text="Subtotal", font=("arial", 12,"bold") , bg="white" ,bd=4)
        lbl_subtotal.grid(row=0  , column=0 , stick = W , padx=5 ,pady=2)
      
        entrySubtotal = ttk.Entry(bottom_frame ,textvariable=self.c_subtotal,font=("arial", 10,"bold"), width=26)
        entrySubtotal.grid(row=0 , column=1,stick = W , padx=5 ,pady=2)

        lbl_tax =Label(bottom_frame,text="Gov Tax", font=("arial", 12,"bold") , bg="white" ,bd=4)
        lbl_tax.grid(row=1  , column=0 , stick = W , padx=5 ,pady=2)
      
        entrytax = ttk.Entry(bottom_frame ,textvariable=self.c_taxtotal,font=("arial", 10,"bold"), width=26)
        entrytax.grid(row=1 , column=1,stick = W , padx=5 ,pady=2)

        lbl_AmountTotal =Label(bottom_frame,text="Total", font=("arial", 12,"bold") , bg="white" ,bd=4)
        lbl_AmountTotal.grid(row=2  , column=0 , stick = W , padx=5 ,pady=2)
      
        entryAmountTotal = ttk.Entry(bottom_frame ,textvariable=self.c_total,font=("arial", 10,"bold"), width=26)
        entryAmountTotal.grid(row=2 , column=1,stick = W , padx=5 ,pady=2)

    #Button Frames for buttons
        btn_frame = Frame(bottom_frame , bd=2 , bg="white")
        btn_frame.place(x=320,y=0)

        #creating buttons

        btnaddtocart =Button(btn_frame, command=self.AddItem,text="Add to Cart" ,font=("arial", 15,"bold"),bg="orangered" ,fg="white",height=2 , width=15, cursor="hand2")
        btnaddtocart.grid(row=0,column=0)

        btnGenerateBill =Button(btn_frame,command=self.gen_bill , text="Generate Bill" ,font=("arial", 15,"bold"),bg="orangered" ,fg="white",height=2 , width=15, cursor="hand2")
        btnGenerateBill.grid(row=0,column=1)

        btnSaveBill =Button(btn_frame, command=self.save_bill,text="Save bill" ,font=("arial", 15,"bold"),bg="orangered" ,fg="white",height=2 , width=15, cursor="hand2")
        btnSaveBill.grid(row=0,column=2)

        btnPrint =Button(btn_frame, command=self.print_bill,text="Print" ,font=("arial", 15,"bold"),bg="orangered" ,fg="white",height=2 , width=15, cursor="hand2")
        btnPrint.grid(row=0,column=3)

        btnClear =Button(btn_frame, command=self.Clear,text="Clear" ,font=("arial", 15,"bold"),bg="orangered" ,fg="white",height=2 , width=15, cursor="hand2")
        btnClear.grid(row=0,column=4)

        btnExit =Button(btn_frame, command=self.root.destroy ,text="Exit" ,font=("arial", 15,"bold"),bg="orangered" ,fg="white",height=2 , width=15, cursor="hand2")
        btnExit.grid(row=0,column=5)

        self.welcome()

        self.list1=[]

#======================= Function Declaration=======================================

    # Defining bill area
    def welcome(self):
        self.textarea.delete(1.0 ,END)
        self.textarea.insert(END , "\t\t\twelcome")
        self.textarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone No. : {self.c_phon.get()}")
        self.textarea.insert(END, f"\n Customer Email : {self.c_email.get()}")

        self.textarea.insert(END,"\n ---------------------------------------------------------------------------------------")
        self.textarea.insert(END, f"\n Products\t\t\t\t Qty\t\tPrice ")
        self.textarea.insert(END,"\n ---------------------------------------------------------------------------------------\n")
        

    def AddItem(self):
        Tax =1
        self.n = self.c_price.get() 
        self.m =self.c_qty.get() * self.n
        self.list1.append(self.m)
        if self.c_product.get() == "":
            messagebox.showerror("Error" , "Select the product name")
        else:
            self.textarea.insert(END , f"\n {self.c_product.get()}\t\t\t\t{self.c_qty.get()}\t\t{self.m}")    
            self.c_subtotal.set(str('Rs.%.2f'%(sum(self.list1))))
            self.c_taxtotal.set(str('Rs.%.2f'%((((sum(self.list1)) - (self.c_price.get()))*Tax)/100)))
            self.c_total.set(str('Rs.%.2f'%((((sum(self.list1)) + ((((sum(self.list1)) - (self.c_price.get()))*Tax)/100))))))


    #Geneting bill 
    def gen_bill(self):
        if self.c_product.get() == "":
            messagebox.showerror("Error" , "Add to cart product")
        else:
            text1 =self.textarea.get(10.0,(10.0+ float(len(self.list1))))
            self.welcome()
            self.textarea.insert(END , text1)
            self.textarea.insert(END,"\n ---------------------------------------------------------------------------------------")
            self.textarea.insert(END , f"\n Sub Amount :\t\t\t{self.c_subtotal.get()}")
            self.textarea.insert(END , f"\n Sub Amount :\t\t\t{self.c_taxtotal.get()}")
            self.textarea.insert(END , f"\n Sub Amount :\t\t\t{self.c_total.get()}")
            self.textarea.insert(END,"\n ---------------------------------------------------------------------------------------")



    #save bill
    def save_bill(self):
        op =messagebox.askyesno("Save Bill" , "Do you want to save the bill ?")
        if op>0:
            self.bill_data = self.textarea.get(1.0, END)
            f1 = open('biils/' + str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            op =messagebox.showinfo("Bill Saved" , f"Bill No . ={self.bill_no.get()} \n Saved Successfully ")
            f1.close()


    #Print bill

    def print_bill(self):
        q = self.textarea.get(1.0,"end-1c")
        filename = tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")


    # search bill function
    def find_bill(self):
        found = "no"
        for i in os.listdir("biils/"):
            if i.split('.')[0]==self.c_search_bill.get():
                f1 = open(f'biils/{i}','r')
                self.textarea.delete(1.0 ,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
            
        if found=="no":
            messagebox.showerror("Error", "Invalid Bill Number")


    # clear bill function
    def Clear(self):
        self.textarea.delete(1.0 , END)
        self.c_name.set("")
        self.c_phon.set("") 
        self.bill_no.set("") 
        x= random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.c_email.set("")
        self.c_search_bill.set("") 
        self.c_product.set(0) 
        self.c_price.set(0)
        self.list1=[0]
        self.c_qty.set("")
        self.c_subtotal.set("") 
        self.c_taxtotal.set("") 
        self.c_total.set("") 
        self.welcome()










    def Categories(self , events=""):
        if self.Combo_Category.get()=="Clothing":
            self.Combo_subcategory.config(value=self.SubcatClothing)
            self.Combo_subcategory.current(0)

        elif self.Combo_Category.get()=="Lifestyles":
            self.Combo_subcategory.config(value=self.SubcatLifestyle)
            self.Combo_subcategory.current(0)

        elif self.Combo_Category.get()=="Mobiles":
            self.Combo_subcategory.config(value=self.SubcatMobiles)
            self.Combo_subcategory.current(0)


    def Product_add(self,event=""):
        if self.Combo_subcategory.get() == "Pant" :
            self.combo_product.config(values=self.Pant)
            self.combo_product.current(0)
            
        elif self.Combo_subcategory.get() == "T-shirt" :
            self.combo_product.config(values=self.Tshirt)
            self.combo_product.current(0)

        elif self.Combo_subcategory.get() == "Shirt" :
            self.combo_product.config(values=self.Shirt)
            self.combo_product.current(0)
            
        elif self.Combo_subcategory.get() == "Bath Soup" :
            self.combo_product.config(values=self.Bathsoup)
            self.combo_product.current(0)

        elif self.Combo_subcategory.get() == "Face Cream" :
            self.combo_product.config(values=self.FaceCream)
            self.combo_product.current(0)
            
        elif self.Combo_subcategory.get() == "Hair Oil" :
            self.combo_product.config(values=self.Hairoil)
            self.combo_product.current(0)

        elif self.Combo_subcategory.get() == "Iphone" :
            self.combo_product.config(values=self.Iphone)
            self.combo_product.current(0)
            
        elif self.Combo_subcategory.get() == "Samsung" :
            self.combo_product.config(values=self.Sumsang)
            self.combo_product.current(0)

        elif self.Combo_subcategory.get() == "oneplus" :
            self.combo_product.config(values=self.Oneplus)
            self.combo_product.current(0)


    def productprice(self,event=""):
        if self.combo_product.get()=="Levis":
            self.combo_price.config(value=self.Price_Levies)
            self.combo_price.current(0)
            self.c_qty.set(1)


        elif self.combo_product.get()=="Mufti":
            self.combo_price.config(value=self.Price_Mufti)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="Spyker":
            self.combo_price.config(value=self.Price_Spyker)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="polo":
            self.combo_price.config(value=self.Price_polo)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="lascoot":
            self.combo_price.config(value=self.Price_lascoot)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="gant":
            self.combo_price.config(value=self.Price_gant)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="Peter England":
            self.combo_price.config(value=self.Price_peterend)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="Louis Phillipe":
            self.combo_price.config(value=self.Price_louisp)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="Park Avenue":
            self.combo_price.config(value=self.Price_parkav)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="Lifeboy":
            self.combo_price.config(value=self.price_lifeboy)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="Santoor":
            self.combo_price.config(value=self.price_santoor)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="Pearls":
            self.combo_price.config(value=self.price_peals)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="Ponds":
            self.combo_price.config(value=self.price_Ponds)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="Fair&lovely":
            self.combo_price.config(value=self.price_Fairlovely)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="Olay":
            self.combo_price.config(value=self.price_Olay)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="Parachute":
            self.combo_price.config(value=self.price_Parachute)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="jasmin":
            self.combo_price.config(value=self.price_jasmin)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="Bajaj":
            self.combo_price.config(value=self.price_Bajaj)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="Iphone 11":
            self.combo_price.config(value=self.price_Iphone11)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="Iphone 12":
            self.combo_price.config(value=self.price_Iphone12)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="Iphone 13":
            self.combo_price.config(value=self.price_Iphone13)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="S1 pro3":
            self.combo_price.config(value=self.price_S1_pro)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="S1 Ultra":
            self.combo_price.config(value=self.price_S1_Ultra)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="Galaxy01":
            self.combo_price.config(value=self.price_Galaxy01)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="oneplusT":
            self.combo_price.config(value=self.price_oneplusT)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="oneplusTpro":
            self.combo_price.config(value=self.price_oneplusTpro)
            self.combo_price.current(0)
            self.c_qty.set(1)

        elif self.combo_product.get()=="oneplus8T":
            self.combo_price.config(value=self.price_oneplus8T)
            self.combo_price.current(0)
            self.c_qty.set(1)






if __name__ == '__main__':
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()
