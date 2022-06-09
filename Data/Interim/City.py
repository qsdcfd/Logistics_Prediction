{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "City",
      "provenance": [],
      "authorship_tag": "ABX9TyP0hfJl9YiZxxqvZfrcm5QR"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "4QNzaGSY52-S"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "seoul = pd.read_csv('/content/TC_NU_SPG_50_METER_11.csv')\n",
        "Busan = pd.read_csv('/content/TC_NU_SPG_50_METER_26.csv')\n",
        "Daegu=  pd.read_csv('/content/TC_NU_SPG_50_METER_27.csv')\n",
        "Incheon =  pd.read_csv('/content/TC_NU_SPG_50_METER_28.csv')\n",
        "Gwangju =  pd.read_csv('/content/TC_NU_SPG_50_METER_29.csv')\n",
        "Daejeon =  pd.read_csv('/content/TC_NU_SPG_50_METER_30.csv')\n",
        "Ulsan =  pd.read_csv('/content/TC_NU_SPG_50_METER_31.csv')\n",
        "Jeolla_do =  pd.read_csv('/content/TC_NU_SPG_50_METER_36.csv')\n",
        "Gyeonggi_do = pd.read_csv('/content/TC_NU_SPG_50_METER_41.csv')\n",
        "Gangwon_do =  pd.read_csv('/content/TC_NU_SPG_50_METER_42.csv')\n",
        "Chungbuk =  pd.read_csv('/content/TC_NU_SPG_50_METER_43.csv')\n",
        "Chungnam = pd.read_csv('/content/TC_NU_SPG_50_METER_44.csv')\n",
        "Jeollabuk= pd.read_csv('/content/TC_NU_SPG_50_METER_45.csv')\n",
        "Jeollanam = pd.read_csv('/content/TC_NU_SPG_50_METER_46.csv')\n",
        "Gyeongsangbuk = pd.read_csv('/content/TC_NU_SPG_50_METER_47.csv')\n",
        "Jeju =  pd.read_csv('/content/TC_NU_SPG_50_METER_50.csv')"
      ],
      "metadata": {
        "id": "QEw61dZY5_Yx"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "Gyeongnam = pd.read_csv('/content/TC_NU_SPG_50_METER_48.csv',encoding='cp949')\n"
      ],
      "metadata": {
        "id": "6oEcH8vf8pCY"
      },
      "execution_count": 70,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def remove(data):\n",
        "    data.drop(columns='격자공간고유번호', inplace=True)\n",
        "    data.drop(columns='격자공간명', inplace=True)\n",
        "    data = data.drop_duplicates(['시군구명'])"
      ],
      "metadata": {
        "id": "twP17kjx-_z7"
      },
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "for i in [Gyeonggi_do, Gangwon_do, Chungbuk, Chungnam,Jeollabuk,Jeollanam,Gyeongsangbuk,Jeju]:\n",
        "    remove(i)\n"
      ],
      "metadata": {
        "id": "tja8rvwzAnpj"
      },
      "execution_count": 38,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "Gyeonggi_do = Gyeonggi_do.drop_duplicates()\n",
        "Gangwon_do = Gangwon_do.drop_duplicates()\n",
        "Chungbuk = Chungbuk.drop_duplicates()\n",
        "Chungnam = Chungnam.drop_duplicates()\n",
        "Jeollabuk = Jeollabuk.drop_duplicates()\n",
        "Jeollanam = Jeollanam.drop_duplicates()\n",
        "Gyeongsangbuk= Gyeongsangbuk.drop_duplicates()\n",
        "Jeju = Jeju.drop_duplicates()\n"
      ],
      "metadata": {
        "id": "oWyp4CxWBxM0"
      },
      "execution_count": 43,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def shapes(j):\n",
        "    print(j.shape)"
      ],
      "metadata": {
        "id": "zQHMDqAjD-J6"
      },
      "execution_count": 44,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "for k in [seoul,Busan,Daegu,Incheon,Gwangju,Daejeon,Ulsan,Jeolla_do ,Gyeonggi_do ,Gangwon_do,Chungbuk ,Chungnam,Jeollanam,Jeollabuk,Gyeongsangbuk ,Jeju]:\n",
        "    print(shapes(k))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5GS5YCxEEEI9",
        "outputId": "202a713a-02ad-44aa-841b-c78a2ab6e49b"
      },
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(25, 2)\n",
            "None\n",
            "(16, 2)\n",
            "None\n",
            "(8, 2)\n",
            "None\n",
            "(8, 2)\n",
            "None\n",
            "(5, 2)\n",
            "None\n",
            "(5, 2)\n",
            "None\n",
            "(5, 2)\n",
            "None\n",
            "(1, 2)\n",
            "None\n",
            "(36, 2)\n",
            "None\n",
            "(7, 2)\n",
            "None\n",
            "(13, 2)\n",
            "None\n",
            "(11, 2)\n",
            "None\n",
            "(9, 2)\n",
            "None\n",
            "(13, 2)\n",
            "None\n",
            "(11, 2)\n",
            "None\n",
            "(2, 2)\n",
            "None\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "City = pd.concat([seoul,Busan,Daegu,Incheon,Gwangju,Daejeon,Ulsan,Jeolla_do ,Gyeonggi_do ,Gangwon_do,Chungbuk ,Chungnam,Jeollanam,Jeollabuk,Gyeongsangbuk ,Jeju,Gyeongnam])\n"
      ],
      "metadata": {
        "id": "tyxAiiOT_9fI"
      },
      "execution_count": 81,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(City)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "K2p-1Kk__9XI",
        "outputId": "3633059a-d1cc-4375-a708-fdeb14e31fb0"
      },
      "execution_count": 82,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "           시군구코드 시군구명\n",
            "0        11500.0  강서구\n",
            "16800    11530.0  구로구\n",
            "23600    11470.0  양천구\n",
            "31200    11440.0  마포구\n",
            "41200    11545.0  금천구\n",
            "...          ...  ...\n",
            "0        48850.0  하동군\n",
            "284800   48860.0  산청군\n",
            "601200   48840.0  남해군\n",
            "806400   48240.0  사천시\n",
            "1006800  48170.0  진주시\n",
            "\n",
            "[180 rows x 2 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "Cities = pd.DataFrame(City)"
      ],
      "metadata": {
        "id": "cIwPJ6qpE8OC"
      },
      "execution_count": 83,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "cities = Cities.dropna()"
      ],
      "metadata": {
        "id": "v-P4-NwGFXyt"
      },
      "execution_count": 84,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "cities = cities.astype({'시군구코드':'int'})\n",
        "cities"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "QxSHZ8T8GQ0r",
        "outputId": "a129b248-ccbf-47b4-e594-e56fdc56247a"
      },
      "execution_count": 67,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "         시군구코드  시군구명\n",
              "0        11500   강서구\n",
              "16800    11530   구로구\n",
              "23600    11470   양천구\n",
              "31200    11440   마포구\n",
              "41200    11545   금천구\n",
              "...        ...   ...\n",
              "1788400  47250   상주시\n",
              "2292000  47280   문경시\n",
              "2516580  47280     문\n",
              "0        50110   제주시\n",
              "452400   50130  서귀포시\n",
              "\n",
              "[172 rows x 2 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-2454581f-0d22-4988-95c3-00639b5aa2a4\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>시군구코드</th>\n",
              "      <th>시군구명</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>11500</td>\n",
              "      <td>강서구</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16800</th>\n",
              "      <td>11530</td>\n",
              "      <td>구로구</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>23600</th>\n",
              "      <td>11470</td>\n",
              "      <td>양천구</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>31200</th>\n",
              "      <td>11440</td>\n",
              "      <td>마포구</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>41200</th>\n",
              "      <td>11545</td>\n",
              "      <td>금천구</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1788400</th>\n",
              "      <td>47250</td>\n",
              "      <td>상주시</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2292000</th>\n",
              "      <td>47280</td>\n",
              "      <td>문경시</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2516580</th>\n",
              "      <td>47280</td>\n",
              "      <td>문</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>50110</td>\n",
              "      <td>제주시</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>452400</th>\n",
              "      <td>50130</td>\n",
              "      <td>서귀포시</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>172 rows × 2 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-2454581f-0d22-4988-95c3-00639b5aa2a4')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-2454581f-0d22-4988-95c3-00639b5aa2a4 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-2454581f-0d22-4988-95c3-00639b5aa2a4');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 67
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cities"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "xZeQefw0Fc_g",
        "outputId": "e2640161-0f8b-4023-ddcf-812ba79db7ec"
      },
      "execution_count": 85,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "           시군구코드 시군구명\n",
              "0        11500.0  강서구\n",
              "16800    11530.0  구로구\n",
              "23600    11470.0  양천구\n",
              "31200    11440.0  마포구\n",
              "41200    11545.0  금천구\n",
              "...          ...  ...\n",
              "0        48850.0  하동군\n",
              "284800   48860.0  산청군\n",
              "601200   48840.0  남해군\n",
              "806400   48240.0  사천시\n",
              "1006800  48170.0  진주시\n",
              "\n",
              "[177 rows x 2 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-96b7f085-131f-45ad-9b1a-f740dcd5b597\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>시군구코드</th>\n",
              "      <th>시군구명</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>11500.0</td>\n",
              "      <td>강서구</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16800</th>\n",
              "      <td>11530.0</td>\n",
              "      <td>구로구</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>23600</th>\n",
              "      <td>11470.0</td>\n",
              "      <td>양천구</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>31200</th>\n",
              "      <td>11440.0</td>\n",
              "      <td>마포구</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>41200</th>\n",
              "      <td>11545.0</td>\n",
              "      <td>금천구</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>48850.0</td>\n",
              "      <td>하동군</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>284800</th>\n",
              "      <td>48860.0</td>\n",
              "      <td>산청군</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>601200</th>\n",
              "      <td>48840.0</td>\n",
              "      <td>남해군</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>806400</th>\n",
              "      <td>48240.0</td>\n",
              "      <td>사천시</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1006800</th>\n",
              "      <td>48170.0</td>\n",
              "      <td>진주시</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>177 rows × 2 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-96b7f085-131f-45ad-9b1a-f740dcd5b597')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-96b7f085-131f-45ad-9b1a-f740dcd5b597 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-96b7f085-131f-45ad-9b1a-f740dcd5b597');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 85
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 전체 열 이름 입력하기\n",
        "cities.columns = ['시군구코드', '시군구명']\n",
        "\n",
        "# 선택하여 열 이름 변경하기\n",
        "cities.rename(columns={'시군구코드':'Send_grid', '시군구명':'Send_state'},inplace=True)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ceG0tiOIGgns",
        "outputId": "75237dcc-2b40-4388-eb22-363144a2e41b"
      },
      "execution_count": 90,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/pandas/core/frame.py:5047: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  errors=errors,\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cities"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "pJDN-PmgJ1WA",
        "outputId": "2efdac1c-e494-4d9b-8ad1-edb66343e8d0"
      },
      "execution_count": 91,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "         Send_grid Send_state\n",
              "0          11500.0        강서구\n",
              "16800      11530.0        구로구\n",
              "23600      11470.0        양천구\n",
              "31200      11440.0        마포구\n",
              "41200      11545.0        금천구\n",
              "...            ...        ...\n",
              "0          48850.0        하동군\n",
              "284800     48860.0        산청군\n",
              "601200     48840.0        남해군\n",
              "806400     48240.0        사천시\n",
              "1006800    48170.0        진주시\n",
              "\n",
              "[177 rows x 2 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-63dea011-1d81-4a18-9990-94a122fe25e4\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Send_grid</th>\n",
              "      <th>Send_state</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>11500.0</td>\n",
              "      <td>강서구</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16800</th>\n",
              "      <td>11530.0</td>\n",
              "      <td>구로구</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>23600</th>\n",
              "      <td>11470.0</td>\n",
              "      <td>양천구</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>31200</th>\n",
              "      <td>11440.0</td>\n",
              "      <td>마포구</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>41200</th>\n",
              "      <td>11545.0</td>\n",
              "      <td>금천구</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>48850.0</td>\n",
              "      <td>하동군</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>284800</th>\n",
              "      <td>48860.0</td>\n",
              "      <td>산청군</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>601200</th>\n",
              "      <td>48840.0</td>\n",
              "      <td>남해군</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>806400</th>\n",
              "      <td>48240.0</td>\n",
              "      <td>사천시</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1006800</th>\n",
              "      <td>48170.0</td>\n",
              "      <td>진주시</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>177 rows × 2 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-63dea011-1d81-4a18-9990-94a122fe25e4')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-63dea011-1d81-4a18-9990-94a122fe25e4 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-63dea011-1d81-4a18-9990-94a122fe25e4');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 91
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cities.to_csv(\"./send_cities.csv\")\n",
        "\n"
      ],
      "metadata": {
        "id": "gGT3PGaLJVxS"
      },
      "execution_count": 92,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#전체 열 이름 입력하기\n",
        "cities.columns = ['Send_grid', 'Send_state']\n",
        "\n",
        "# 선택하여 열 이름 변경하기\n",
        "cities.rename(columns={'Send_grid':'Rec_grid', 'Send_state':'Rec_state'},inplace=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9uxvw_L6JV00",
        "outputId": "16344931-b86b-4a79-cea4-153d138eb171"
      },
      "execution_count": 95,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/pandas/core/frame.py:5047: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  errors=errors,\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cities.to_csv(\"./rec_cities.csv\")\n"
      ],
      "metadata": {
        "id": "AyqYLsPOKQ8-"
      },
      "execution_count": 96,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        ""
      ],
      "metadata": {
        "id": "o-EnOB1x8g-I"
      }
    }
  ]
}