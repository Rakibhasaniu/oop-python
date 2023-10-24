from School import School,ClassRoom



def main():
    school = School('Rakib','Bogura')


    eight = ClassRoom('eight')
    school.add_classroom(eight)

    nine = ClassRoom('nine')
    school.add_classroom(nine)

    ten = ClassRoom('ten')
    school.add_classroom(ten)

    print(school)


if __name__ == '__main__':
    main()