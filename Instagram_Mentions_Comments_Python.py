# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 03:29:38 2024

@author: Harikrishnan Nair
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time

# Configuration
instagram_url = "https://www.instagram.com"
username = "dtp2148"
password = "HKNAIR"  # Updated password to match the initial code
post_url = "https://www.instagram.com/p/CPGDLfAANbI/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=="  # Replace with the actual post URL

# Give the Input Tags starting with '@'
# Also make sure that the tags placed in this variable are not recorded under spam activity...
input_tags = [
    "o.faby , athulyaseethu6_ , samarth_3383 ",
    "mrs_su_xx_ni_ , ashok_choudhary4456_ , stylish_muhajir ",
    "the_dopehead_ , anna_xabu_ , notty.xgirl_0 ",
    "g.s.e_fx_ , crooz_x , malikedit5 ",
    "yoko.boy__ , x_habibbi_ , v3_boys___7256 ",
    "grey_attma_ , aaaaaan1134 , mrs_mickeymack ",
    "the_apex_ , darkshine04_ , aasha_viswanath ",
    "rosevin_britto_ , editors_choice_videos_ , akshaaa_y ",
    "jerith2021_ , ajay.ashin_ , zesty_dragon_856 ",
    "mrs_black_axle_ , bushra_binth_abdulrahman_ , unaiz___mohd ",
    "v.shumi_ , f_a_rha_n_7_ , dieselpunk ",
    "ameen_amuneer_ , aaliyyahhh_ , ar.xmal ",
    "x_max_n_ , alan_2000_23_ , abh__ij_ith ",
    "abishhkarr__ , tamilnadudigitalagency_ , alarif_000 ",
    "lu_ff_yy_ , .anshiyo._ , v_i_x_h_u ",
    "shyamr3124_ , ajmal_khan.a , _erfxn_7 ",
    "e_ventor_ , mohd_fayaas_ , ni_ya_s_11 ",
    "mhd_afslllll_ , mxhxdevxn_ , aleemi.ftw ",
    "surbin_samuel_ , ricky_2oo3_ , i.b.z.z ",
    "itz.nikk_ , theroggerff_ , berwin_linnet_ ",
    "akshay..sajin_ , der_win_143_ , anzil..__ ",
    "arath.i , adhiii._ , ajmal.r.s ",
    "ajmina , .shahinaaaah._ , .hashim_muhammed. ",
    "farhan.ahmd , j1n0yss_ , baba_huss_ain ",
    ".mohammed_sha_ , nayan.z_ , n.ova.__ ",
    "m_uflih._ , haseeeee_b_ , vr_asgardianz ",
    "sree_nxn_dh_ , _alvviinn , the_epic_gurl_26 ",
    "ajxth._ , jin_z_ben_ , ft.anzil_ ",
    "aro_malzz_ , arx_thy._ , alfizz ",
    "akhil_sr2003_ , albin.antony._ , rohanbm. ",
    "alan.appuz_ , fayaaaah_ , _ydhxxu ",
    "mr_s_m_o_k_e_ , shx_hxi_b , fati._mah ",
    "popeyye._ , zenitsu_v4 , fxyx_z ",
    "fayaaa_d_ , sarath_sr666_ , bonjeee_ ",
    "hari_krishnan8055_ , x_eron__ , syam_jose22 ",
    "moh.shazin_ , diora.art_ , machan_fx ",
    "gayathri_.aravind_ , ajmxl_sha_ , ana.nyahh ",
    "nasiha_habeeb_ , ashif.s , far_x_an ",
    "aromal_s_s , meera_s_hari , harieiiii ",
    "mr_x_chu_ , vipinmithravs_ , jain_james__ ",
    "firox_7_ , noufal3150_ , .athira._ ",
    "muhammed_bin_ashraf_ , haritha_harilal_ , suhais__ ",
    "kalidax._ , abhirwm_ , fazil.as ",
    "z..ayaa..n_ , adhil_mxhd._ , uj.thx_6 ",
    "al.a_n___ , sayd_sabiq_ , nihx.l_niche_ ",
    "aleena_aleee_ , .gokul.g._ , afffzal__ ",
    "mhd_ashkar._ , shammi.i_ , iam_rih_an ",
    "ajay_ks_2_ , i_4bi_vs_ , zammil__zain ",
    "nikhil_krishna_js_ , banacafe_ , _x_jayson ",
    "a_f_i_n , .chelsy.541 , ares007_ ",
    "v_is_h_n_u_j_b228_ , joel_joy_lfc_ , renotyser"
]

# Convert tags to tag sets
tag_sets = [tag_set.split(",") for tag_set in input_tags]

# Path to chromedriver executable
chromedriver_path = r"C:\Users\Harikrishnan Nair\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Initialize the WebDriver using the Service object
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open Instagram and log in
    driver.get(instagram_url)
    time.sleep(3)  # Wait for the page to load

    # Enter username
    username_input = driver.find_element(By.NAME, 'username')
    username_input.send_keys(username)

    # Enter password
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(password)

    # Submit login form
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)  # Wait for login to complete

    # Navigate to the post
    driver.get(post_url)
    time.sleep(3)  # Wait for the post to load

    # Find the comment box and enter the comments
    for tag_set in tag_sets:
        comment_text = " , ".join(tag_set)
        while True:
            try:
                comment_box = driver.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Add a comment…"]')
                comment_box.click()
                comment_box.send_keys(comment_text)
                time.sleep(3)  # Adding 3 seconds delay before posting the comment
                # Post the comment
                comment_box.send_keys(Keys.RETURN)
                break  # Exit the loop if successful
            except StaleElementReferenceException:
                time.sleep(1)  # Wait a bit before trying again
            except NoSuchElementException:
                time.sleep(1)  # Wait a bit before trying again

        time.sleep(3)  # Wait for 3 seconds after posting each set of comments

finally:
    # Close the WebDriver
    driver.quit()
