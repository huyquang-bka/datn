brands = ['0____Aston Martin', '1____Audi', '2____Bentley', '3____Bmw', '4____Chevrolet', '5____Ford', '6____Honda',
          '7____Hyundai', '8____Isuzu', '9____Jaguar', '10____Kia', '11____Lamborghini', '12____LandRover',
          '13____Lexus', '14____Maserati', '15____Mazda', '16____MercedesBenz', '17____Minicoopers', '18____Mitsubishi',
          '19____Nissan', '20____Peugeot', '21____Porsche', '22____SSangYong', '23____subaru', '24____Suzuki',
          '25____Toyota', '26____vinfast', '27____Volkswagen', '28____Volvo', '29____Daewoo']

with open('brands.txt', 'w') as f:
    for brand in brands:
        f.write(brand.split("____")[-1] + '\n')
