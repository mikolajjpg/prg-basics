def main():

    ms_to_kmh = lambda ms: ms * 3.6

    v1 = 10
    v2 = 35

    print(f"{v1} m/s = {int(ms_to_kmh(v1))} km/h")
    print(f"{v2} m/s = {int(ms_to_kmh(v2))} km/h")


if __name__ == "__main__":
    main()