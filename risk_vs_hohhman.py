import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

data = np.array([[0.7400888980631123, 0.5935118837938044, 0.4994190244640774], [0.9837987601785259, 0.974530205889378, 0.9637530386841], [0.9997293050086661, 0.9631472392150917, 0.9702550770669485], [0.4996989181263244, 0.1261091184324148, 0.15035305566249862], [0.7867576553228769, 0.46870723237638934, 0.45235873360643375], [0.9304074903685129, 0.867801470179322, 0.8320086884798217], [0.18477243389340747, 0.18370261155742362, 0.0641090296987138], [0.13420733228830273, 0.05112215882750348, 0.03233024130330706], [0.29174595647532287, 0.755800864717923, 0.23475066824066984], [0.8063224711866555, 0.46357876441581725, 0.46029967416806555], [0.323677657392044, 0.5327744515565841, 0.20269328059694175], [0.03939111134909956, 0.6998612969047099, 0.029932873690058835], [0.04049194585226312, 0.5822587411225719, 0.02695982070448628], [0.47725666208503315, 0.6670561538448146, 0.3501369271428119], [0.4105916902484248, 0.11821223435473405, 0.12094790693908748], [0.34057444771721246, 0.5093413103834346, 0.2068897979301621], [0.8846461696290187, 0.11357339040114156, 0.25730704575792457], [0.04182866973844357, 0.018957651922008156, 0.009000112636698353], [0.4827926196123856, 0.8589188172034312, 0.4283022565560902], [0.5897451327719073, 0.1451956463545102, 0.18645176714417627], [0.6785217869419654, 0.6707954348033118, 0.4998238110645977], [0.8082740868859578, 0.7033105801059198, 0.6164289909230681], [0.4989019076876492, 0.4885691421926849, 0.2947788431993289], [0.8968353961284413, 0.7858012002227763, 0.7431545437696869], [0.7549974374530876, 0.01811153877733307, 0.16193881978279248], [0.2826541098360851, 0.06704351110449014, 0.0716909211284373], [0.933310360887219, 0.1685847240130165, 0.3125355678643723], [0.2928524324047841, 0.1925099335324395, 0.10367208831860339], [0.26684275612374675, 0.5835144006933979, 0.17793382395988744], [0.2645127718023844, 0.5516567904142925, 0.16963876773335013], [0.9910758984584579, 0.8055909215952689, 0.8369365768196981], [0.5294029346577701, 0.3458810810069092, 0.25236895439368173], [0.19711570117881883, 0.1311392515703056, 0.06010282465604081], [0.8016785057553092, 0.015372124083617433, 0.17019450232357353], [0.8378465138397093, 0.9792812516728115, 0.8239592089940636], [0.35867461403409207, 0.8518058908356988, 0.3161518421087866], [0.8874608457499769, 0.24901067447687586, 0.3542819481676117], [0.22565045113145044, 0.2675821099104171, 0.09343410927908287], [0.7439500641605116, 0.14923745858053983, 0.23761018634101774], [0.9092670441200659, 0.6418788766751174, 0.6487648559260071], [0.8120426740771658, 0.4775349025561826, 0.4726315102049542], [0.7915334475466178, 0.5498260589980851, 0.5064712623331031], [0.2977305175182, 0.3584247104535281, 0.14491728313135194], [0.45062909656005, 0.40225719113240044, 0.23514085501183155], [0.45036322789362926, 0.9128579045503066, 0.4189667515799183], [0.8531542850903961, 0.9278554728507351, 0.8039139551038236], [0.8894875347461054, 0.7601992223699293, 0.718847692726609], [0.6520407866936491, 0.145927021257946, 0.20652845313144338], [0.7681783748647112, 0.28936433643288406, 0.33146241553679695], [0.08435673540363209, 0.09153656442829239, 0.023048727676914404], [0.5161066310959472, 0.4241857468228476, 0.2783613876205161], [0.5615183455497904, 0.7380812621128308, 0.4438606044562764], [0.49358110561960233, 0.35502072547076813, 0.2389014388805085], [0.21440368541144628, 0.2978477734418117, 0.09396846533630358], [0.3459840614737144, 0.12615287332276182, 0.1041143190777734], [0.5648167109798358, 0.8687619049321957, 0.5055163356106708], [0.058314505412673245, 0.6310870658084792, 0.041104125174499954], [0.2302392530974382, 0.23601512299179128, 0.08951980712935168], [0.5420026385035309, 0.172523268792113, 0.18320698121156948], [0.679360502688019, 0.11204515387539604, 0.19676734218604017], [0.46608626199599923, 0.864261732017707, 0.4154736684490567], [0.06479048914469665, 0.29866226076853863, 0.028438477000342976], [0.46150734524461023, 0.7933544386959696, 0.3852125897214059], [0.7308200729590056, 0.8448988363489859, 0.640139237970637], [0.7164154325899866, 0.3999209012654926, 0.3724906909035135], [0.5034880403223874, 0.8570410609090171, 0.44590554745079813], [0.42339270488987757, 0.7848191042333624, 0.35050788769046676], [0.8991632886302429, 0.5225636957856022, 0.5557287307031333], [0.5834159123341238, 0.6490245235411136, 0.41960417008999185], [0.9385990832215351, 0.1098622672693017, 0.2702131153159917], [0.42945867172289776, 0.6618288095848298, 0.31327423152237766], [0.44031203859573853, 0.03964541418859502, 0.10202749023302986], [0.7641162374036974, 0.07177006396962671, 0.19669578447169453], [0.8535619982073952, 0.7807472366987055, 0.7038453368026385], [0.524648490194636, 0.5187180630115087, 0.3226454169154665], [0.8319296290534556, 0.8980023441943694, 0.7640457314864953], [0.8371646848429238, 0.49348944827866925, 0.49793848772180116], [0.8523058800222326, 0.4271099591061437, 0.46168383965422377], [0.12147042644507788, 0.0421876253736897, 0.028393724364893395], [0.45912459417742635, 0.7953756309292083, 0.383966129850675], [0.5940865799316656, 0.22160254247236055, 0.2241381932355862], [0.9835483039656827, 0.5590237512121551, 0.6365711506981356], [0.6631348199281428, 0.1774016482221049, 0.2267399320246056], [0.4276248889819182, 0.33605770689015524, 0.20049028947672012], [0.04790413762244783, 0.8492869986066487, 0.04212831653425641], [0.29424962544127864, 0.7131499495014945, 0.22672520950768096], [0.3582674095416434, 0.877556203198354, 0.32317331202598815], [0.9991534710465999, 0.7335330683356279, 0.7861603832933243], [0.27238055072413503, 0.7461623371418376, 0.21706819680106815], [0.6497894782833618, 0.3659410702625152, 0.3201856213593402], [0.1463300426194898, 0.49318346924376655, 0.0870000549828325], [0.5660026202133461, 0.3951601611668659, 0.2921298733421686], [0.7284697275015476, 0.24332419610280442, 0.287497394163944], [0.7300489433175926, 0.952021235530973, 0.7020274662757552], [0.9131676195661054, 0.5898095536164356, 0.6135095127718353], [0.677969016869089, 0.2940765745418452, 0.2950936482749091], [0.02799949202218488, 0.8123830628364636, 0.02379694887391512], [0.222187738421888, 0.8126682493627017, 0.18888948401491648], [0.000898416160504345, 0.8864680881777921, 0.0008168170370531243], [0.31960024600478376, 0.39704602818294976, 0.1654368558269512]])

X = data[:, :2]
y = data[:, 2]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Sequential()
model.add(Dense(1, input_dim=2, activation='linear'))

model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(X_train, y_train, epochs=100, batch_size=1, verbose=1)
model.save('risk_vs_hohhman.keras')

loss = model.evaluate(X_test, y_test)
print(f'Test Loss: {loss}')

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
print(f'Mean Absolute Error (MAE): {mae}')

mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error (MSE): {mse}')

rmse = np.sqrt(mse)
print(f'Root Mean Squared Error (RMSE): {rmse}')

r2 = r2_score(y_test, predictions)
print(f'R-squared (R²): {r2}')