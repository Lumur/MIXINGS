import os, sys



print ("\033[1;32mMasukin UserName&Password:)")

print ("\033[1;32m?? HUBUNGI LANGSUNG Mr.MBEST √")

username = 'mbest'      

password = 'sempak'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print ("\033[1;32mZONA MERAH TELAH DIMULAI\033[00m")

			sys.exit()



		else:

			print ("\033[1;32mSorry Passwordmu salah tod !!!\033[00m")

			print ("Login Maning\n")

			restart()



	else:

		print ("\033[1;32mSorry..anda noob !!!\033[00m")

		print ("Login Maning\n")

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()

