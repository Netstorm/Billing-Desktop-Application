from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1370x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #============================VARIABLES==================================================================#
        #============================Cosmetics variables===============================================#
        self.bath=IntVar()
        self.fC=IntVar()
        self.fW = IntVar()
        self.hS=IntVar()
        self.hG = IntVar()
        self.bL = IntVar()
        #==========================Grocery variables======================================================#
        self.rice = IntVar()
        self.foodoil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar = IntVar()
        self.tea= IntVar()
        #===========================Cold Drink variables====================================================#
        self.maza  = IntVar()
        self.cock=IntVar()
        self.frooti = IntVar()
        self.pepsi = IntVar()
        self.limca= IntVar()
        self.sprite= IntVar()
        #===============================Bill Menu============================================================#
        self.cosmetic_price=StringVar()
        self.grocery_price = StringVar()
        self.colddrink_price = StringVar()


        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.colddrink_tax = StringVar()

        #==============================Customer==============================================================#
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()


        #===============================CUSTOMER DETAILS FRAME==============================================#
        f1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",fg="gold",bg=bg_color,font=("Times new roman",20,"bold"))
        f1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(f1,text="Customer name",bg=bg_color,fg="white",font=("times new roman",19,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(f1,width=15,textvariable=self.c_name,bd=7,font=("arial",15)).grid(row=0,column=1,padx=10,pady=5)

        cphone = Label(f1, text="Phone No.", bg=bg_color, fg="white", font=("times new roman", 19, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphone_txt = Entry(f1, width=15,textvariable=self.c_phone, bd=7, font=("arial", 15)).grid(row=0, column=3, padx=10, pady=5)

        cbill = Label(f1, text="Bill No.", bg=bg_color, fg="white", font=("times new roman", 19, "bold")).grid(row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(f1, width=15,textvariable=self.bill_no, bd=7, font=("arial", 15)).grid(row=0, column=5, padx=10, pady=5)

        bill_btn=Button(f1,text="Search",command=self.find_bill,font=('arial',12,'bold'),bd=7).grid(row=0,column=6,padx=10,pady=10)

        #=================================COSMETICS FRAME==================================================================#
        f2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",fg="gold",bg=bg_color,font=("Times new roman",20,"bold"))
        f2.place(x=5,y=180,width=325,height=350)
        bath_lb1=Label(f2,text="Bath Soap",font=("times new roman" ,19 ,'bold'),bg=bg_color,fg="white").grid(row=0,column=0)
        bath_txt=Entry(f2,width=10,textvariable=self.bath,bd=7,font=("arial",15)).grid(row=0,column=1,padx=10,pady=5)

        face_cream_lb1=Label(f2,text="Face Cream",font=("times new roman" ,19 ,'bold'),bg=bg_color,fg="white").grid(row=1,column=0)
        face_cream_txt=Entry(f2,width=10,textvariable=self.fC, bd=7,font=("arial",15)).grid(row=1,column=1,padx=10,pady=5)

        face_wash_lb1 = Label(f2, text="Face wash", font=("times new roman", 19, 'bold'), bg=bg_color, fg="white").grid(row=2, column=0)
        face_wash_txt = Entry(f2, width=10,textvariable=self.fW, bd=7, font=("arial", 15)).grid(row=2, column=1,padx=10,pady=5)

        hair_s_lb1 = Label(f2, text="Hair Shampoo", font=("times new roman", 19, 'bold'), bg=bg_color, fg="white").grid(row=3, column=0)
        hair_s_txt = Entry(f2, width=10,textvariable=self.hS, bd=7, font=("arial", 15)).grid(row=3, column=1,padx=10,pady=5)

        hair_g_lb1 = Label(f2, text="Hair Gel", font=("times new roman", 19, 'bold'), bg=bg_color, fg="white").grid(row=4, column=0)
        hair_g_txt = Entry(f2, width=10,textvariable=self.hG, bd=7, font=("arial", 15)).grid(row=4, column=1,padx=10,pady=5)

        body_lb1 = Label(f2, text="Body lotion", font=("times new roman", 19, 'bold'), bg=bg_color, fg="white").grid(row=5, column=0)
        body_txt = Entry(f2, width=10,textvariable=self.bL, bd=7, font=("arial", 15)).grid(row=5, column=1,padx=10,pady=5)

        #==================================GROCERY FRAME========================================================================#

        f3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery ",bg=bg_color,fg="gold",font=("Times new roman",20,"bold"))
        f3.place(x=340,y=180,width=325,height=350)
        rice_lb1=Label(f3,text="Rice",font=("times new roman" ,19 ,'bold'),bg=bg_color,fg="white").grid(row=0,column=0)
        rice_txt=Entry(f3,width=13,textvariable=self.rice,bd=7,font=("arial",15)).grid(row=0,column=1,padx=10,pady=5)

        foodoil_lb1=Label(f3,text="Food Oil",font=("times new roman" ,19 ,'bold'),bg=bg_color,fg="white").grid(row=1,column=0)
        foodoil_cream_txt=Entry(f3,width=13,textvariable=self.foodoil,bd=7,font=("arial",15)).grid(row=1,column=1,padx=10,pady=5)

        daal_lb1 = Label(f3, text="Daal", font=("times new roman", 19, 'bold'), bg=bg_color, fg="white").grid(row=2, column=0)
        daalwash_txt = Entry(f3, width=13,textvariable=self.daal, bd=7, font=("arial", 15)).grid(row=2, column=1,padx=10,pady=5)

        wheat_lb1 = Label(f3, text="Wheat", font=("times new roman", 19, 'bold'), bg=bg_color, fg="white").grid(row=3, column=0)
        wheat_txt = Entry(f3, width=13,textvariable=self.wheat, bd=7, font=("arial", 15)).grid(row=3, column=1,padx=10,pady=5)

        sugar_lb1 = Label(f3, text="Sugar", font=("times new roman", 19, 'bold'), bg=bg_color, fg="white").grid(row=4, column=0)
        sugar_txt = Entry(f3, width=13,textvariable=self.sugar, bd=7, font=("arial", 15)).grid(row=4, column=1,padx=10,pady=5)

        tea_lb1 = Label(f3, text="Tea", font=("times new roman", 19, 'bold'), bg=bg_color, fg="white").grid(row=5, column=0)
        tea_txt = Entry(f3, width=13,textvariable=self.tea, bd=7, font=("arial", 15)).grid(row=5, column=1,padx=10,pady=5)

        #===========================================COLD DRINK=======================================================================================#

        f4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drink", fg="gold", bg=bg_color,font=("Times new roman", 20, "bold"))
        f4.place(x=680, y=180, width=325, height=350)
        maza_lb1 = Label(f4, text="Maza", font=("times new roman", 19, 'bold'), bg=bg_color, fg="white").grid(row=0, column=0)
        maza_txt = Entry(f4, width=13,textvariable=self.maza, bd=7, font=("arial", 15)).grid(row=0, column=1, padx=10, pady=5)

        cock_lb1 = Label(f4, text="Cock", font=("times new roman", 19, 'bold'), bg=bg_color,fg="white").grid(row=1, column=0)
        cock_cream_txt = Entry(f4, width=13,textvariable=self.cock, bd=7, font=("arial", 15)).grid(row=1, column=1, padx=10, pady=5)

        frooti_lb1 = Label(f4, text="Frooti", font=("times new roman", 19, 'bold'), bg=bg_color, fg="white").grid(row=2, column=0)
        frooti_wash_txt = Entry(f4, width=13,textvariable=self.frooti, bd=7, font=("arial", 15)).grid(row=2, column=1, padx=10, pady=5)

        pepsi_lb1 = Label(f4, text="Pepsi", font=("times new roman", 19, 'bold'), bg=bg_color, fg="white").grid(row=3, column=0)
        pepsi_txt = Entry(f4, width=13,textvariable=self.pepsi, bd=7, font=("arial", 15)).grid(row=3, column=1, padx=10, pady=5)

        limca_lb1 = Label(f4, text="Limca", font=("times new roman", 19, 'bold'), bg=bg_color, fg="white").grid(row=4, column=0)
        limca_txt = Entry(f4, width=13,textvariable=self.limca, bd=7, font=("arial", 15)).grid(row=4, column=1, padx=10, pady=5)

        sprite_lb1 = Label(f4, text="sprite", font=("times new roman", 19, 'bold'), bg=bg_color, fg="white").grid(row=5, column=0)
        sprite_txt = Entry(f4, width=13,textvariable=self.sprite, bd=7, font=("arial", 15)).grid(row=5, column=1, padx=10, pady=5)
        #======================================BILL AREA==============================================================================#

        f5 = Frame(self.root, bd=10, relief=GROOVE)
        f5.place(x=1010, y=180, width=380, height=350)
        bill_title=Label(f5,font=('arial',15,'bold'),text="Bill Area",bd=7,relief=GROOVE).pack(fill=X)
        scrolbar=Scrollbar(f5,orient=VERTICAL)
        self.textarea=Text(f5,yscrollcommand=scrolbar.set)
        scrolbar.pack(side=RIGHT,fill=Y)
        scrolbar.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH)

        #=================================BUTTON FRAME========================================#
        f6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", fg="gold", bg=bg_color,font=("Times new roman", 20, "bold"))
        f6.place(x=0, y=520, relwidth=1, height=180)
        tcp_lb1=Label(f6,text="Total cosmetics price",font=("times new roman",15,"bold"),fg="white",bg=bg_color).grid(row=0,column=0)
        tcp_txt=Entry(f6,textvariable=self.cosmetic_price, font=("arial",15,"bold"),bd=7,fg="black").grid(row=0,column=1,padx=5,pady=5)

        tgp_lb1=Label(f6,text="Total grocery price",font=("times new roman",15,"bold"),fg="white",bg=bg_color).grid(row=1,column=0)
        tgp_txt=Entry(f6,textvariable=self.grocery_price,font=("arial",15,"bold"),bd=7,fg="black").grid(row=1,column=1,padx=5,pady=5)

        tcdp_lb1=Label(f6,text="Total cold drink price",font=("times new roman",15,"bold"),fg="white",bg=bg_color).grid(row=2,column=0)
        tcdp_txt=Entry(f6,textvariable=self.colddrink_price,font=("arial",15,"bold"),bd=7,fg="black").grid(row=2,column=1,padx=5,pady=5)

        costax_lb1=Label(f6,text="Cometic Tax",font=("times new roman",15,"bold"),fg="white",bg=bg_color).grid(row=0,column=2)
        costtax_txt=Entry(f6,textvariable=self.cosmetic_tax,font=("arial",15,"bold"),bd=7,fg="black").grid(row=0,column=3,padx=5,pady=5)

        grotax_lb1=Label(f6,text="Grocery Tax",font=("times new roman",15,"bold"),fg="white",bg=bg_color).grid(row=1,column=2)
        grotax_txt=Entry(f6,textvariable=self.grocery_tax,font=("arial",15,"bold"),bd=7,fg="black").grid(row=1,column=3,padx=5,pady=5)

        codtax_lb1=Label(f6,text="cold drink Tax",font=("times new roman",15,"bold"),fg="white",bg=bg_color).grid(row=2,column=2)
        codtax_txt=Entry(f6,textvariable=self.colddrink_tax,font=("arial",15,"bold"),bd=7,fg="black").grid(row=2,column=3,padx=5,pady=5)

        btn_frame = Frame(f6, bd=10, relief=GROOVE)
        btn_frame.place(x=820, width=520, height=130)

        total_btn=Button(btn_frame,text="Total",command=self.total,font=("arial",15,"bold"),fg='cadetblue',bd=7,bg=bg_color,width=8,height=2).grid(row=0,column=0,padx=5,pady=5)
        Gn_btn=Button(btn_frame,text="GeneratBill",command=self.bill_area,font=("arial",15,"bold"),fg='cadetblue',bd=7,bg=bg_color,width=8,height=2).grid(row=0,column=1,padx=5,pady=5)
        clear_btn = Button(btn_frame, text="Clear", command=self.clear_data,font=("arial", 15, "bold"), fg='cadetblue', bd=7, bg=bg_color,width=8, height=2).grid(row=0, column=2, padx=5, pady=5)
        exit_btn = Button(btn_frame, text="Exit", command=self.Exit_app,font=("arial", 15, "bold"), fg='cadetblue', bd=7, bg=bg_color,width=8, height=2).grid(row=0, column=3, padx=5, pady=5)

    def total(self):
        self.c_bs_p=self.bath.get()*40
        self.c_fC_p=self.fC.get()*70
        self.c_fW_p = self.fW.get() * 100
        self.c_hS_p = self.hS.get() * 50
        self.c_hG_p = self.hG.get() * 30
        self.c_bL_p=self.bL.get()*80

        self.total_cosmetic_price = float(
                                         self.c_bs_p+
                                         self.c_fC_p+
                                         self.c_fW_p+
                                         self.c_hS_p+
                                         self.c_hG_p+
                                         self.c_bL_p
                                        )
        self.cosmetic_price.set("Rs."+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs."+str(self.c_tax))

        self.c_rice_p=self.rice.get()*25
        self.c_foodoil_p = self.foodoil.get() *90
        self.c_daal_p = self.daal.get() * 50
        self.c_wheat_p = self.wheat.get() * 27
        self.c_sugar_p = self.sugar.get() * 22
        self.c_tea_p=self.tea.get()*75

        self.total_grocery_price = float(
                                         self.c_rice_p+
                                         self.c_foodoil_p+
                                         self.c_daal_p+
                                         self.c_wheat_p+
                                         self.c_sugar_p +
                                         self.c_tea_p
                                        )
        self.grocery_price.set("Rs."+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.05),2)
        self.grocery_tax.set("Rs."+str(self.g_tax))

        self.c_maza_p=self.maza.get()*20
        self.c_cock_p = self.cock.get() *30
        self.c_frooti_p = self.frooti.get() *20
        self.c_pepsi_p = self.pepsi.get() * 40
        self.c_limca_p = self.limca.get() * 40
        self.c_sprite_p = self.sprite.get() *30
        self.total_colddrink_price = float(
                                            self.c_maza_p +
                                            self.c_cock_p+
                                            self.c_frooti_p +
                                            self.c_pepsi_p +
                                            self.c_limca_p+
                                            self.c_sprite_p
                                           )
        self.colddrink_price.set("Rs."+str(self.total_colddrink_price))
        self.cd_tax=round((self.total_colddrink_price*0.05),2)
        self.colddrink_tax.set("Rs."+str(self.cd_tax))

        self.Total_Bill=float(self.total_cosmetic_price+
                              self.total_grocery_price+
                              self.total_colddrink_price+
                              self.c_tax+
                              self.g_tax+
                              self.cd_tax)




    def welcome_bill(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\tWelcome Webcode Retail")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n==========================================")
        self.textarea.insert(END,f"\nProduct\t\tQTY\t\tPrice")
        self.textarea.insert(END,f"\n==========================================")


    def bill_area(self):

        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must.")
        elif self.cosmetic_price.get()== "Rs.0.0"  and  self.grocery_price.get()== "Rs.0.0" and self.colddrink_price.get()=="Rs.0.0":
            messagebox.showerror("Error","No Products are purchsed")
        else:
            self.welcome_bill()
            #==========================COSMETICS===========================================#
            if self.bath.get()!=0:
                self.textarea.insert(END,f"\n Bath Soap\t\t {self.bath.get()}\t\t{self.c_bs_p}")
            if self.fC.get() != 0:
                self.textarea.insert(END, f"\n Face Cream\t\t {self.fC.get()}\t\t{self.c_fC_p}")
            if self.fW.get() != 0:
                self.textarea.insert(END, f"\n Face Wash \t\t {self.fW.get()}\t\t{self.c_fW_p}")
            if self.hS.get() != 0:
                self.textarea.insert(END, f"\n Hair Shampoo\t\t {self.hS.get()}\t\t{self.c_hS_p}")
            if self.hG.get()!=0:
                self.textarea.insert(END,f"\n Hair Gel\t\t {self.hG.get()}\t\t{self.c_hG_p}")
            if self.bL.get() != 0:
                self.textarea.insert(END, f"\n Body Lotion\t\t {self.bL.get()}\t\t{self.c_bL_p}")
            #===========================GROCERY===================================================#
            if self.rice.get()!=0:
                self.textarea.insert(END,f"\n Rice\t\t {self.rice.get()}\t\t{self.c_rice_p}")
            if self.foodoil.get() != 0:
                self.textarea.insert(END, f"\n Food Oil\t\t {self.foodoil.get()}\t\t{self.c_foodoil_p}")
            if self.daal.get() != 0:
                self.textarea.insert(END, f"\n Daal \t\t {self.daal.get()}\t\t{self.c_daal_p}")
            if self.wheat.get() != 0:
                self.textarea.insert(END, f"\n Wheat\t\t {self.wheat.get()}\t\t{self.c_wheat_p}")
            if self.sugar.get()!=0:
                self.textarea.insert(END,f"\n Sugar\t\t {self.sugar.get()}\t\t{self.c_sugar_p}")
            if self.tea.get() != 0:
                self.textarea.insert(END, f"\n Tea \t\t {self.tea.get()}\t\t{self.c_tea_p}")
             #===================================COLDDRINK===========================================#

            if self.maza.get()!=0:
                self.textarea.insert(END,f"\n Maza \t\t {self.maza.get()}\t\t{self.c_maza_p}")
            if self.cock.get() != 0:
                self.textarea.insert(END, f"\n Cock \t\t {self.cock.get()}\t\t{self.c_cock_p}")
            if self.frooti.get() != 0:
                self.textarea.insert(END, f"\n Frooti \t\t {self.frooti.get()}\t\t{self.c_frooti_p}")
            if self.pepsi.get() != 0:
                self.textarea.insert(END, f"\n Pepsi\t\t {self.pepsi.get()}\t\t{self.c_pepsi_p}")
            if self.limca.get()!=0:
                self.textarea.insert(END,f"\n Limca\t\t {self.limca.get()}\t\t{self.c_limca_p}")
            if self.sprite.get() != 0:
                self.textarea.insert(END, f"\n Sprite\t\t {self.sprite.get()}\t\t{self.c_sprite_p}")


            self.textarea.insert(END,f"\n------------------------------------------")
            if self.cosmetic_tax.get()!= "Rs.0.0":
                self.textarea.insert(END,f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!= "Rs.0.0":
                self.textarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")

            if self.colddrink_tax.get()!= "Rs.0.0":
                self.textarea.insert(END,f"\n Cold Drink Tax\t\t\t{self.colddrink_tax.get()}")
            self.textarea.insert(END, f"\n------------------------------------------")

            self.textarea.insert(END,f"\n Total Bill\t\t\t Rs. {self.Total_Bill}")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.textarea.get("1.0",END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no.: {self.bill_no.get()} saved Successfully")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid bill number")

    def clear_data(self):
        op=messagebox.askyesno("Clear","D you want to clear?")
        if op>0:
            self.bath.set(0)
            self.fC.set(0)
            self.fW.set(0)
            self.hS.set(0)
            self.hG.set(0)
            self.bL.set(0)
        # ==========================Grocery variables======================================================#
            self.rice.set(0)
            self.foodoil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
        # ===========================Cold Drink variables====================================================#
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.pepsi.set(0)
            self.limca.set(0)
            self.sprite.set(0)
        # ===============================Bill Menu============================================================#
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.colddrink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.colddrink_tax.set("")

        # ==============================Customer==============================================================#
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()


    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()

root=Tk()
obj = Bill_App(root)
root.mainloop()