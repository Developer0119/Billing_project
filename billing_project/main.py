from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow


class Bill_App:
     def __init__(self,root):
          self.root=root
          self.root.geometry("1110x620+80+20")  #size of page
          self.root.title("Billing systam")   #name of page
         
         #image
          #img=Image.open("image//shopname.jpg")
          #img=img.resize((1230,50),Image)
          #self.photoimg=ImageTk.PhotoIMage(img)
          
          #lbl_img=Label(self.root,image=self.photoimg) 
          #lbl_img.place(x=0,y=0,width=1230,height=50)
         
 #title
          lbl_title=Label(self.root,text="MY STOR BILLING SYSTAM",font=("timesnew roman",30,"bold"),bg="white",fg="red")
          lbl_title.place(x=0,y=0,width=1230,height=35)
          
#main frame
          main_frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
          main_frame.place(x=5,y=35,width=1100,height=580)

 #costomer label frame
          Cust_Frame=LabelFrame(main_frame,text="Customer",font=("time new roman",15,"bold"),bg="white",fg="red")
          Cust_Frame.place(x=10,y=5,width=650,height=150)
          
      #mobile number
          self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("time new rowan",15,"bold"),bg="white")
          self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

          self.entry_mob=ttk.Entry(Cust_Frame,font=("time new roman",15,"bold"),width=42)
          self.entry_mob.grid(row=0,column=1)
 
     #name
          self.lbl_name=Label(Cust_Frame,text="Full Name",font=("time new rowan",15,"bold"),bg="white")
          self.lbl_name.grid(row=1,column=0,sticky=W,padx=5,pady=5)

          self.entry_name=ttk.Entry(Cust_Frame,font=("time new roman",15,"bold"),width=42)
          self.entry_name.grid(row=1,column=1,sticky=W,padx=5,pady=5)
     #Email
          self.lbl_email=Label(Cust_Frame,text="Email/Gmail",font=("time new rowan",15,"bold"),bg="white")
          self.lbl_email.grid(row=2,column=0,sticky=W,padx=5,pady=5)

          self.entry_email=ttk.Entry(Cust_Frame,font=("time new roman",15,"bold"),width=42)
          self.entry_email.grid(row=2,column=1,sticky=W,padx=5,pady=5)

 #product Label frame
          product_Frame=LabelFrame(main_frame,text="Product",font=("time new roman",15,"bold"),bg="white",fg="red")
          product_Frame.place(x=10,y=155,width=650,height=300)

     #category
          self.lbl_category=Label(product_Frame,text="Select Category",font=("time new rowan",15,"bold"),bg="white")
          self.lbl_category.grid(row=0,column=0,sticky=W,padx=5,pady=7)
          
          self.Combo_Category=ttk.Combobox(product_Frame,font=("time new rowan",15,"bold"),width=40,state="readonly")
          self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=7)

     #subcategory
          self.lbl_subcategory=Label(product_Frame,text="Subcategory",font=("time new rowan",15,"bold"),bg="white")
          self.lbl_subcategory.grid(row=1,column=0,sticky=W,padx=5,pady=7)
          
          self.Combo_subcategory=ttk.Combobox(product_Frame,font=("time new rowan",15,"bold"),width=40,state="readonly")
          self.Combo_subcategory.grid(row=1,column=1,sticky=W,padx=5,pady=7)

     #product name
          self.lbl_product_name=Label(product_Frame,text="Product Name",font=("time new rowan",15,"bold"),bg="white")
          self.lbl_product_name.grid(row=2,column=0,sticky=W,padx=5,pady=7)
          
          self.Combo_product_name=ttk.Combobox(product_Frame,font=("time new rowan",15,"bold"),width=40,state="readonly")
          self.Combo_product_name.grid(row=2,column=1,sticky=W,padx=5,pady=7)
     #price
          self.lbl_price=Label(product_Frame,text="Price",font=("time new rowan",15,"bold"),bg="white")
          self.lbl_price.grid(row=3,column=0,sticky=W,padx=5,pady=7)
          
          self.Combo_price=ttk.Combobox(product_Frame,font=("time new rowan",15,"bold"),width=40,state="readonly")
          self.Combo_price.grid(row=3,column=1,sticky=W,padx=5,pady=7)

     #Qty
          self.lbl_Qty=Label(product_Frame,text="Qty in product",font=("time new rowan",15,"bold"),bg="white")
          self.lbl_Qty.grid(row=4,column=0,sticky=W,padx=5,pady=7)

          self.entry_Qty=ttk.Entry(product_Frame,font=("time new roman",15,"bold"),width=42)
          self.entry_Qty.grid(row=4,column=1)

#search aria
         
          search_frame=Frame(main_frame,bd=2,bg="white")
          search_frame.place(x=680,y=10,width=390,height=40)

          self.lbl_search=Label(search_frame,text="Bill no.",font=("time new rowan",18,"bold"),bg="black",fg="white",width=7)
          self.lbl_search.grid(row=0,column=0,sticky=W,padx=5,pady=2)

          self.entry_search=ttk.Entry(search_frame,font=("time new roman",18,"bold"),width=15)
          self.entry_search.grid(row=0,column=1)
 
          self.Btnsearch=Button(search_frame,text="search",font=("time new roman",12,"bold"),bg="black",fg="red",width=5,cursor="hand2")
          self.Btnsearch.grid(row=0,column=2,sticky=W,padx=5,pady=2)
          
          


#Billing aria
          Bill_Frame=LabelFrame(main_frame,text="Product",font=("time new roman",15,"bold"),bg="white",fg="red")
          Bill_Frame.place(x=670,y=50,width=400,height=510)

          scroll_y=Scrollbar(Bill_Frame,orient=VERTICAL)
          self.textarea=Text(Bill_Frame,yscrollcommand=scroll_y,font=("time new roman",18,"bold"),bg="white",fg="red")
          scroll_y.pack(side=RIGHT,fill=Y)
          scroll_y.config(command=self.textarea.yview)
          self.textarea.pack(fill=BOTH,expand=1)

 #bill countar
          Cust_Frame=LabelFrame(main_frame,text="Customer",font=("time new roman",15,"bold"),bg="white",fg="red")
          Cust_Frame.place(x=10,y=460,width=650,height=110)
          
       
     #sub total
          self.sub_total=Label(Cust_Frame,text="Sub Total",font=("time new rowan",10,"bold"),bg="white")
          self.sub_total.grid(row=0,column=0,sticky=W,padx=0,pady=1)

          self.entry_Qty=ttk.Entry(Cust_Frame,font=("time new roman",10,"bold"),width=23)
          self.entry_Qty.grid(row=0,column=1)
     #gov_tax
          self.gov_tax=Label(Cust_Frame,text="GovTax",font=("time new rowan",10,"bold"),bg="white")
          self.gov_tax.grid(row=1,column=0,sticky=W,padx=0,pady=1)

          self.gov_tax=ttk.Entry(Cust_Frame,font=("time new roman",10,"bold"),width=23)
          self.gov_tax.grid(row=1,column=1)

     #total_bill
          self.total_bill=Label(Cust_Frame,text="Total Bill",font=("time new rowan",10,"bold"),bg="white")
          self.total_bill.grid(row=2,column=0,sticky=W,padx=0,pady=1)

          self.total_bill=ttk.Entry(Cust_Frame,font=("time new roman",10,"bold"),width=23)
          self.total_bill.grid(row=2,column=1)
#Botton Fram
          Btn_frame=Frame(Cust_Frame,bd=2,bg="white")
          Btn_frame.place(x=250,y=0)
          
          self.BtnaddtoCard=Button(Btn_frame,text="Add To Card",font=("time new roman",12,"bold"),bg="black",fg="white",width=10,cursor="hand2")
          self.BtnaddtoCard.grid(row=0,column=0,sticky=W,padx=8,pady=0)
          
          self.BtnGenerateBill=Button(Btn_frame,text="Generate Bill",font=("time new roman",12,"bold"),bg="black",fg="white",width=10,cursor="hand2")
          self.BtnGenerateBill.grid(row=0,column=1,sticky=W,padx=8,pady=2)
          
          self.BtnSaveBill=Button(Btn_frame,text="Save Bill",font=("time new roman",12,"bold"),bg="black",fg="white",width=10,cursor="hand2")
          self.BtnSaveBill.grid(row=0,column=2,sticky=W,padx=8,pady=2)
          
          self.Btnprint=Button(Btn_frame,text="Print",font=("time new roman",12,"bold"),bg="black",fg="white",width=10,cursor="hand2")
          self.Btnprint.grid(row=1,column=0,sticky=W,padx=8,pady=2)
          
          self.BtnClear=Button(Btn_frame,text="Clear",font=("time new roman",12,"bold"),bg="black",fg="white",width=10,cursor="hand2")
          self.BtnClear.grid(row=1,column=1,sticky=W,padx=8,pady=2)
          
          self.BtnExit=Button(Btn_frame,text="Exit",font=("time new roman",12,"bold"),bg="red",fg="white",width=10,cursor="hand2")
          self.BtnExit.grid(row=1,column=2,sticky=W,padx=8,pady=2)
          
          

 



if __name__=='__main__':
     root=Tk()
     obj=Bill_App(root)
     root.mainloop()
          