import { FormControl } from "@angular/forms"

export interface Video {
    id: number,
    title: string,
    blob?: Blob,
    size?: number
}

export interface VideoForm {
    id?: FormControl<number | null>,
    title: FormControl<string | null>,
    file: FormControl<File | null>,
    description: FormControl<string | null>
    size?: FormControl<number | null>
}
