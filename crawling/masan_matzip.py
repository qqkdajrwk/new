import sys
import os
import pandas as pd

from bs4 import BeauifulSoup as bs
import time
from tqdm.notebook import tqdm
from selenium import webdriver

webdriver.Chrome('http://www.naver.com')